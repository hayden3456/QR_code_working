## Logging for API Requests and Responses

This application now includes logging for API requests and responses to enhance traceability and debugging. Logging is configured to output at the INFO level, capturing key events such as the generation of AI prompts, API request details, and the success or failure of image processing.

### Enabling Logging

Logging is enabled by default. The logs are printed to the standard output, which can be redirected to a file if needed.

### Example Log Entries

- **Generated AI Prompt**: Logs the AI prompt generated for image creation.
  ```
  INFO:root:Generated AI prompt: <prompt details>
  ```

- **API Request Details**: Logs the details of the API request, including the seed used.
  ```
  INFO:root:API request sent with seed: <seed number>
  ```

- **Successful Image Processing**: Logs when an image is processed successfully.
  ```
  INFO:root:Image processed successfully
  ```

- **Error in Image Processing**: Logs any errors encountered during image processing.
  ```
  ERROR:root:Error processing image: <error details>
  ```

### Viewing Logs

To view the logs, ensure your application is running and check the console output. If you wish to save logs to a file, you can redirect the standard output to a file using shell redirection.

```bash
python main.py > app.log 2>&1
```
