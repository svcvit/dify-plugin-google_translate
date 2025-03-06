# Google Translate Plugin

## google_translate

**Author:** svcvit
**Version:** 0.0.1
**Type:** plugin

### Description

A powerful translation tool plugin based on Google Translate service, supporting text translation between multiple languages.

### Features

- Automatic source language detection
- Support for multiple target languages
- No API key required
- Fast response and accurate translation

### Usage Guide

#### Parameters

1. **content** (Required)
   - Type: string
   - Description: Text content to be translated
   - Example: `"Hello World"`

2. **dest** (Required)
   - Type: string
   - Description: Target language code
   - Supported language codes:
     - ar: Arabic
     - bg: Bulgarian
     - ca: Catalan
     - zh-cn: Chinese (Simplified)
     - zh-tw: Chinese (Traditional)
     - cs: Czech
     - da: Danish
     - nl: Dutch
     - en: English
     ...

#### Response Format

The plugin returns the translated text content. In case of any errors during translation, it will return the corresponding error message.

#### Example Usage

```python
# Example parameters
parameters = {
    "content": "Hello, world",
    "dest": "zh-cn"
}

# Expected output
"你好，世界"