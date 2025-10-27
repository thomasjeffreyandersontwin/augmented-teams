#!/bin/bash

# Test feature detection logic
echo "🧪 Testing feature detection..."
echo ""

# Test case 1: Changed features/test-feature/main.py
echo "📝 Test 1: Changed features/test-feature/main.py"
CHANGED_FILES="features/test-feature/main.py"

FEATURES=$(echo "$CHANGED_FILES" | grep '^features/[^/]*/' | grep -v '^features/containerization/' | cut -d'/' -f2 | sort -u | grep -v "^$" | tr '\n' ' ')
echo "Detected: $FEATURES"
if [ "$FEATURES" == "test-feature" ]; then
  echo "✅ PASS"
else
  echo "❌ FAIL"
fi
echo ""

# Test case 2: Multiple features
echo "📝 Test 2: Changed features/test-feature/main.py and features/git-integration/config/provision-service.py"
CHANGED_FILES="features/test-feature/main.py
features/git-integration/config/provision-service.py"

FEATURES=$(echo "$CHANGED_FILES" | grep '^features/[^/]*/' | grep -v '^features/containerization/' | cut -d'/' -f2 | sort -u | grep -v "^$" | tr '\n' ' ')
echo "Detected: $FEATURES"
if [[ "$FEATURES" == *"test-feature"* ]] && [[ "$FEATURES" == *"git-integration"* ]]; then
  echo "✅ PASS"
else
  echo "❌ FAIL"
fi
echo ""

# Test case 3: Skip containerization subdirectories
echo "📝 Test 3: Changed features/containerization/something.py (should be skipped)"
CHANGED_FILES="features/containerization/something.py"

FEATURES=$(echo "$CHANGED_FILES" | grep '^features/[^/]*/' | grep -v '^features/containerization/' | cut -d'/' -f2 | sort -u | grep -v "^$" | tr '\n' ' ')
echo "Detected: '$FEATURES'"
if [ -z "$FEATURES" ]; then
  echo "✅ PASS (correctly skipped)"
else
  echo "❌ FAIL"
fi
echo ""

echo "✅ Detection tests complete!"

