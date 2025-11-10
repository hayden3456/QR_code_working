## Configuration Options

The application can retrieve the OpenAI API key from either an environment variable or a configuration file. This provides flexibility in managing API keys.

### Environment Variables

- `OPENAI_API_KEY`: The API key for accessing OpenAI services. If this is not set, the application will attempt to retrieve the key from the configuration file.

### Configuration File

The application supports reading the API key from a `config.ini` file located in the root directory. The file should have the following structure:

```ini
[API_KEYS]
OPENAI_API_KEY=your_openai_api_key_here
```

Ensure that the `config.ini` file is properly configured with the necessary API keys under the `[API_KEYS]` section.
