# Frontend Behavior and Error Handling

The `templates/index.html` implements client-side validation, user feedback, and request retry.

## Form Validation
- `#text1` (URL)
  - Required (HTML5 `required`)
  - Empty values are blocked with an inline error
- `#text2` (Industry)
  - Required (HTML5 `required`)
  - Max length 200 (HTML5 `maxlength="200"`)
  - Client-side length check mirrors backend

## Error Display
- Element: `#errorMessage`
  - Hidden by default, shown when errors occur
  - Displays:
    - Backend errors from `response.error`
    - Network errors
    - 400/500 series errors with user-friendly messages
    - Timeout errors (after 2 minutes)
- Helper functions:
  - `showError(message)`
  - `hideError()`

## Requests and Timeouts
- AJAX call via `makeApiRequest(data)`:
  - Endpoint: `/api`
  - Method: POST
  - Timeout: 120,000 ms (2 minutes)
  - Success:
    - If `response.ImageBytes` present: display image in `#resultImage` and show `#redoContainer`
    - If `response.error` present: show error
  - Error: show user-friendly message depending on `xhr.status` and `status` (e.g., timeout, 400, 500)

## Redo Flow
- The last submitted form data is stored in `formData`
- Clicking `#redo`:
  - Re-sends the previous request if available
  - If no prior request exists, an error is shown

## Loading Indicator
- `#loading` is shown during requests and hidden on completion/error.
