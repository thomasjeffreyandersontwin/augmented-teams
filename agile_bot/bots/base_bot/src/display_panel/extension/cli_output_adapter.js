class CLIOutputAdapter {
  adapt(rawOutput) {
    return {
      bot: this._extractBotInfo(rawOutput),
      behaviors: this._extractBehaviorsHierarchy(rawOutput),
      session: this._extractSessionState(rawOutput),
      scope: this._extractScopeSection(rawOutput),
      parameters: this._extractParameters(rawOutput),
      runExamples: this._extractRunExamples(rawOutput),
      headless: this._extractHeadless(rawOutput),
      commands: this._extractCommands(rawOutput)
    };
  }

  _extractBotInfo(rawOutput) {
    // AC: WHEN CLI outputs bot section THEN panel reads bot name
    const botMatch = /##[^B]*Bot:\s*(.+)/m.exec(rawOutput);
    const botName = botMatch ? botMatch[1].trim() : null;
    
    // AC: WHEN CLI outputs bot section THEN panel reads bot directory path
    const botPathMatch = /\*\*Bot Path:\*\*[^\n]*\n\s*```\s*\n\s*(.+?)\s*\n\s*```/s.exec(rawOutput);
    const botDirectory = botPathMatch ? botPathMatch[1].trim() : '';
    
    // AC: WHEN CLI outputs bot section THEN panel reads workspace name AND workspace directory path
    const workspaceMatch = /Workspace:\*\*\s+(.+?)\s*\n\s*```\s*(.+?)```/s.exec(rawOutput);
    const workspaceName = workspaceMatch ? workspaceMatch[1].trim() : '';
    const workspaceDirectory = workspaceMatch ? workspaceMatch[2].trim() : '';
    
    // AC: WHEN bot section is missing THEN panel shows "unknown bot" message
    return {
      name: botName || 'unknown bot',
      botDirectory: botDirectory,
      workspaceName: workspaceName,
      workspaceDirectory: workspaceDirectory
    };
  }

  _extractBehaviorsHierarchy(rawOutput) {
    // Extract section starting with ## 📍 **Progress** (with emoji)
    const progressSection = this._extractSection(rawOutput, '##.*Progress', '────');
    if (!progressSection) return [];
    const lines = progressSection.split('\n');
    const behaviors = [];
    let currentBehavior = null;
    let currentAction = null;
    for (const line of lines) {
      // Match behavior: "- ➤ shape - Description"
      if (/^- [➤☑☐] \w+/.test(line)) {
        const match = /^- ([➤☑☐]) (\w+)(?:\s+-\s+(.+))?/.exec(line);
        if (match) {
          currentBehavior = {
            name: match[2],
            description: match[3] || '',
            isCurrent: match[1] === '➤',
            isCompleted: match[1] === '☑',
            status: match[1] === '➤' ? 'current' : match[1] === '☑' ? 'completed' : 'pending',
            actions: []
          };
          behaviors.push(currentBehavior);
          currentAction = null;
        }
      }
      // Match action: "  - ☑ clarify"
      else if (/^  - [➤☑☐] \w+/.test(line)) {
        const match = /^  - ([➤☑☐]) (\w+)(?:\s+-\s+(.+))?/.exec(line);
        if (match && currentBehavior) {
          currentAction = {
            name: match[2],
            description: match[3] || '',
            isCurrent: match[1] === '➤',
            isCompleted: match[1] === '☑',
            status: match[1] === '➤' ? 'current' : match[1] === '☑' ? 'completed' : 'pending',
            operations: []
          };
          currentBehavior.actions.push(currentAction);
        }
      }
      // Match operation: "    - ➤ instructions"
      else if (/^    - [➤☑☐] \w+/.test(line)) {
        const match = /^    - ([➤☑☐]) (\w+)/.exec(line);
        if (match && currentAction) {
          currentAction.operations.push({
            name: match[2],
            isCurrent: match[1] === '➤',
            isCompleted: match[1] === '☑',
            status: match[1] === '➤' ? 'current' : match[1] === '☑' ? 'completed' : 'pending'
          });
        }
      }
    }
    return behaviors;
  }

  _extractSessionState(rawOutput) {
    const positionMatch = /Current Position[^\n]*```\s*(.+?)\s*```/s.exec(rawOutput);
    if (!positionMatch) {
      return { currentPosition: '', currentBehavior: '', currentAction: '', actionPhase: '', progressPath: '' };
    }
    const position = positionMatch[1].trim();
    const parts = position.split('.');
    return {
      currentPosition: position,
      currentBehavior: parts[0] || '',
      currentAction: parts[1] || '',
      actionPhase: parts[2] || '',
      progressPath: parts.slice(0, 2).join('.')
    };
  }

  _extractScopeSection(rawOutput) {
    // AC: Extract scope section from CLI output - now expects JSON format
    // Look for JSON code block in scope section (between ``` markers)
    const scopeJsonMatch = /```json\s*\n([\s\S]+?)\n```/m.exec(rawOutput);
    
    if (scopeJsonMatch) {
      try {
        const scopeData = JSON.parse(scopeJsonMatch[1]);
    
        // Convert JSON format to existing panel format
        const graphLinks = [];
        if (scopeData.links) {
          if (scopeData.links.graph) {
            graphLinks.push({ text: 'Graph', url: scopeData.links.graph });
          }
          if (scopeData.links.map) {
            graphLinks.push({ text: 'map', url: scopeData.links.map });
          }
        }
        
        // Determine type and content based on JSON structure
        if (scopeData.type === 'files' || scopeData.type === 'FILES') {
          return {
            type: 'files',
            filter: scopeData.filter,
            graphLinks: graphLinks,
            content: scopeData.files || []
          };
        } else if (scopeData.storyGraph && scopeData.storyGraph.epics) {
          // Convert story graph epics to panel format
          const epics = (scopeData.storyGraph.epics || []).map(epic => ({
            icon: '🎯',
            type: 'epic',
            name: epic.name,
            features: (epic.sub_epics || []).map(subEpic => {
              // Collect stories from both story_groups and direct stories array
              const allStories = [];
              
              // Get stories from story_groups
              if (subEpic.story_groups && Array.isArray(subEpic.story_groups)) {
                subEpic.story_groups.forEach(group => {
                  if (group.stories && Array.isArray(group.stories)) {
                    allStories.push(...group.stories);
                  }
                });
              }
              
              // Get stories directly at sub_epic level
              if (subEpic.stories && Array.isArray(subEpic.stories)) {
                allStories.push(...subEpic.stories);
              }
              
              return {
                icon: '⚙️',
                type: 'feature',
                name: subEpic.name,
                links: subEpic.test_file ? [{ text: 'Test', url: subEpic.test_file }] : [],
                stories: allStories.map(story => {
                  const storyLinks = [];
                  
                  // Debug: Log story properties
                  console.log(`Story: ${story.name}, has story_file: ${!!story.story_file}, story_file_exists: ${story.story_file_exists}, story_file value: ${story.story_file}`);
                  
                  // Use story_file from JSON if available and exists
                  if (story.story_file && story.story_file_exists) {
                    console.log(`Adding story link for ${story.name}: ${story.story_file}`);
                    storyLinks.push({ text: 'Story', url: story.story_file });
                  }
                  
                  // Add test file link if available
                  if (story.test_file) {
                    storyLinks.push({ text: 'Test', url: story.test_file });
                  }
                  
                  console.log(`Story ${story.name} final links:`, storyLinks);
                  
                  return {
                    icon: '📝',
                    type: 'story',
                    name: story.name,
                    storyFile: story.story_file,
                    storyFileExists: story.story_file_exists,
                    testFile: story.test_file,
                    testClass: story.test_class,
                    links: storyLinks
                  };
                })
              };
            })
          }));
          
          return {
            type: 'story',
            filter: scopeData.filter,
            graphLinks: graphLinks,
            content: epics
          };
        } else {
          // Type is 'all' or unknown
          return {
            type: 'all',
            filter: scopeData.filter || 'all (entire project)',
            graphLinks: graphLinks,
            content: null
          };
    }
      } catch (e) {
        // JSON parse failed, fall back to default
        console.error('Failed to parse scope JSON:', e);
        return { type: 'all', filter: 'all (entire project)', content: null };
      }
    }
    
    // No JSON found - return default
    return { type: 'all', filter: 'all (entire project)', content: null };
  }

  _extractStoryTree(scopeSection) {
    const epics = [];
    const lines = scopeSection.split('\n');
    let currentEpic = null;
    let currentFeature = null;
    for (const line of lines) {
      if (/🎯/.test(line) && !line.includes('Current Scope:')) {
        const name = line.replace(/^[^🎯]*🎯 /, '').trim();
        currentEpic = { icon: '🎯', type: 'epic', name: name, features: [] };
        epics.push(currentEpic);
        currentFeature = null;
      }
      else if (/⚙️/.test(line) && currentEpic) {
        const match = /⚙️ (.+?)(?:\s*\|)?/.exec(line);
        if (match) {
          currentFeature = { icon: '⚙️', type: 'feature', name: match[1].trim(), links: this._extractLinks(line), stories: [] };
          currentEpic.features.push(currentFeature);
        }
      }
      else if (/📝/.test(line) && currentFeature) {
        const nameMatch = /📝 (.+?)[\]\|]/.exec(line);
        if (nameMatch) {
          currentFeature.stories.push({ icon: '📝', type: 'story', name: nameMatch[1].trim(), links: this._extractLinks(line) });
        }
      }
    }
    return epics;
  }

  _extractFileList(scopeSection) {
    const files = [];
    const lines = scopeSection.split('\n');
    let inFileList = false;
    for (const line of lines) {
      if (line.includes('Files in scope:')) {
        inFileList = true;
        continue;
      }
      if (inFileList && line.trim().startsWith('- ')) {
        const path = line.trim().substring(2).trim();
        files.push({ path: path, type: path.split('.').pop() });
      }
    }
    return files;
  }

  _extractLinks(text) {
    const links = [];
    const linkRegex = /\[([^\]]+)\]\(([^)]+)\)/g;
    let match;
    while ((match = linkRegex.exec(text)) !== null) {
      links.push({ text: match[1], url: match[2] });
    }
    return links;
  }

  _extractParameters(rawOutput) {
    const argsSection = this._extractCodeBlock(rawOutput, 'Args:');
    if (!argsSection) return [];
    const parameters = [];
    const lines = argsSection.split('\n');
    for (const line of lines) {
      const match = /^(--\S+)\s*(?:"([^"]+)")?\s*#\s*(.+)/.exec(line.trim());
      if (match) {
        parameters.push({ flag: match[1], syntax: match[2] || '', description: match[3] });
      }
    }
    return parameters;
  }

  _extractRunExamples(rawOutput) {
    const runSection = this._extractCodeBlock(rawOutput, 'Run:');
    if (!runSection) return [];
    const examples = [];
    const lines = runSection.split('\n');
    for (const line of lines) {
      const trimmed = line.trim();
      if (!trimmed || trimmed.startsWith('//')) continue;
      const parts = trimmed.split('#');
      examples.push({ command: parts[0].trim(), description: parts[1] ? parts[1].trim() : '' });
    }
    return examples;
  }

  _extractHeadless(rawOutput) {
    const headlessSection = this._extractSection(rawOutput, 'Headless Mode:', '────');
    if (!headlessSection) return { status: 'unavailable' };
    const statusMatch = /Status: (.+)/m.exec(headlessSection);
    const apiKeyMatch = /API Key: (.+)/m.exec(headlessSection);
    const sessionIdMatch = /Session ID: (.+)/m.exec(headlessSection);
    const logMatch = /Log: (.+)/m.exec(headlessSection);
    const result = {
      status: statusMatch ? statusMatch[1].trim() : 'unavailable',
      apiKey: apiKeyMatch ? apiKeyMatch[1].trim() : ''
    };
    if (sessionIdMatch) {
      result.activeSession = { sessionId: sessionIdMatch[1].trim(), logPath: logMatch ? logMatch[1].trim() : '' };
    }
    return result;
  }

  _extractCommands(rawOutput) {
    const commandMatch = /Commands[^\n]*\*\*(.+?)\*\*/s.exec(rawOutput);
    if (!commandMatch) return { text: '', list: [] };
    const commandText = commandMatch[1].trim();
    const commandList = commandText.split('|').map(cmd => cmd.trim());
    return { text: commandText, list: commandList };
  }

  _extractSection(text, startMarker, endMarker) {
    const startRegex = new RegExp(startMarker, 'i');
    const startMatch = startRegex.exec(text);
    if (!startMatch) return null;
    const startPos = startMatch.index + startMatch[0].length;
    const remaining = text.substring(startPos);
    const endRegex = new RegExp(endMarker, 'i');
    const endMatch = endRegex.exec(remaining);
    if (endMatch) return remaining.substring(0, endMatch.index);
    return remaining;
  }

  _extractCodeBlock(text, precedingText) {
    const regex = new RegExp(precedingText + '\\s*```[^`]*?\\n([\\s\\S]+?)```', 'i');
    const match = regex.exec(text);
    return match ? match[1].trim() : null;
  }
}

module.exports = CLIOutputAdapter;
