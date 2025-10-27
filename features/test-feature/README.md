# Test Containerization Feature

This is a test feature for lifecycle automation testing.

## Files

- `main.py` - Main Flask service
- `integration.py` - Integration functions
- `config/config.yaml` - Feature configuration
- `requirements.txt` - Dependencies
- `test-service.py` - Test suite

## Usage

```bash
# Run inject-config
python features/containerization/inject-config.py features/test-features/test-containerization

# Build Docker image
docker build -t test-containerization:latest -f features/test-features/test-containerization/config/Dockerfile features/test-features/test-containerization/

# Run locally
docker run -p 8000:8000 test-containerization:latest

# Test
python features/test-features/test-containerization/test-service.py
```

