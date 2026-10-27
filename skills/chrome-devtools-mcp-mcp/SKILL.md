---
name: chrome-devtools-mcp-mcp
description: >-
  Use when you need to debug or profile a live web page in Chrome — recording performance traces, inspecting network requests and console errors with source-mapped stack traces, or automating and screenshotting real browser behavior.
---

# Chrome DevTools MCP Tools

Chrome DevTools for agents (chrome-devtools-mcp) lets your coding agent (such as Antigravity, Claude, Cursor or Copilot) control and inspect a live Chrome browser. It acts as a Model-Context-Protocol (MCP) server, giving your AI coding assistant access to the full power of Chrome DevTools for reliable automation, in-depth debugging, and performance analysis.

## How to Call Tools

```bash
python3 scripts/call-tool.py <tool_name> '<arguments_json>'
```

## Tools

### click

Clicks on the provided element

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| dblClick | boolean | No | Set to true for double clicks. Default is false. |
| includeSnapshot | boolean | No | Whether to include a snapshot in the response. Default is false. |
| pageId | number | Yes | Targets a specific page by ID. |
| uid | string | Yes | The uid of an element on the page from the page content snapshot |

**Example:**
```bash
python3 scripts/call-tool.py click '{"dblClick":true,"includeSnapshot":true,"pageId":0,"uid":"..."}'
```

---

### close_page

Closes the page by its index. The last open page cannot be closed.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| pageId | number | Yes | The ID of the page to close. Call list_pages to list pages. |

**Example:**
```bash
python3 scripts/call-tool.py close_page '{"pageId":0}'
```

---

### drag

Drag an element onto another element

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| from_uid | string | Yes | The uid of the element to drag |
| includeSnapshot | boolean | No | Whether to include a snapshot in the response. Default is false. |
| pageId | number | Yes | Targets a specific page by ID. |
| to_uid | string | Yes | The uid of the element to drop into |

**Example:**
```bash
python3 scripts/call-tool.py drag '{"from_uid":"...","includeSnapshot":true,"pageId":0,"to_uid":"..."}'
```

---

### emulate

Emulates various features on the target page.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| colorScheme | string | No | Emulate the dark or the light mode. Set to "auto" to reset to the default. |
| cpuThrottlingRate | number | No | Represents the CPU slowdown factor. Omit or set the rate to 1 to disable throttling |
| extraHttpHeaders | string | No | Extra HTTP headers as a JSON string object, e.g. {"X-Custom": "value", "Authorization": "Bearer token"}. Headers are included into every HTTP request originating from the page and persist across navigations until cleared. Pass an empty string to clear all extra headers. |
| geolocation | string | No | Geolocation (`<latitude>,<longitude>`) to emulate. Latitude between -90 and 90. Longitude between -180 and 180. Omit to clear the geolocation override. |
| networkConditions | string | No | Throttle network. Omit to disable throttling. |
| pageId | number | Yes | Targets a specific page by ID. |
| userAgent | string | No | User agent to emulate. Set to empty string to clear the user agent override. |
| viewport | string | No | Emulate device viewports '<width>x<height>x<devicePixelRatio>[,mobile][,touch][,landscape]'. 'touch' and 'mobile' to emulate mobile devices. 'landscape' to emulate landscape mode. |

**Example:**
```bash
python3 scripts/call-tool.py emulate '{"colorScheme":"...","cpuThrottlingRate":0,"extraHttpHeaders":"...","geolocation":"...","networkConditions":"...","pageId":0,"userAgent":"...","viewport":"..."}'
```

---

### evaluate_script

Evaluate a JavaScript function inside the target page. Returns the response as JSON, so returned values have to be JSON-serializable.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| args | array<string> | No | An optional list of arguments to pass to the function. |
| dialogAction | string | No | Handle dialogs while execution. "accept", "dismiss", or string for response of window.prompt. Defaults to accept. |
| filePath | string | No | The absolute or relative path to a file to save the script output to. If omitted, the output is returned inline. |
| function | string | Yes | A JavaScript function declaration to be executed by the tool in the target page.
Example without arguments: `() => document.title` or `async () => await fetch("example.com")`.
Example with arguments: `(el) => el.innerText`
 |
| pageId | number | Yes | Targets a specific page by ID. |
| waitForStableDom | boolean | No | Whether to wait for the DOM to settle. Pass false if the script only reads data. Defaults to true. |

**Example:**
```bash
python3 scripts/call-tool.py evaluate_script '{"args":[],"dialogAction":"...","filePath":"...","function":"...","pageId":0,"waitForStableDom":true}'
```

---

### fill

Type text into an input, text area or select an option from a <select> element.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| includeSnapshot | boolean | No | Whether to include a snapshot in the response. Default is false. |
| pageId | number | Yes | Targets a specific page by ID. |
| uid | string | Yes | The uid of an element on the page from the page content snapshot |
| value | string | Yes | The value to fill in. "true" or "false" for checkboxes and toggles, "true" for radio buttons. |

**Example:**
```bash
python3 scripts/call-tool.py fill '{"includeSnapshot":true,"pageId":0,"uid":"...","value":"..."}'
```

---

### fill_form

Fill out multiple form elements (inputs, selects, checkboxes, radios) at once. ALWAYS prefer this tool over multiple individual 'fill' or 'click' calls when interacting with forms. It is significantly faster, more reliable, and reduces turn count. Example: Fill username, password, and check "Remember Me" in one call.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| elements | array<object> | Yes | Elements from snapshot to fill out. |
| includeSnapshot | boolean | No | Whether to include a snapshot in the response. Default is false. |
| pageId | number | Yes | Targets a specific page by ID. |

**Example:**
```bash
python3 scripts/call-tool.py fill_form '{"elements":[],"includeSnapshot":true,"pageId":0}'
```

---

### get_console_message

Gets a console message by its ID. You can get all messages by calling list_console_messages.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| msgid | number | Yes | The msgid of a console message on the page from the listed console messages |
| pageId | number | Yes | Targets a specific page by ID. |

**Example:**
```bash
python3 scripts/call-tool.py get_console_message '{"msgid":0,"pageId":0}'
```

---

### get_css_styles

Retrieve matched CSS rules, inline styles, inherited styles, and cascade information for an element identified by its UID.
Use this tool to debug why specific CSS properties are applied, overridden, or conflicting. Results are paginated and return 10 rules per page by default; use pageIdx to page through the remaining rules. Requires a UID from take_snapshot.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| pageId | number | Yes | Targets a specific page by ID. |
| pageIdx | integer | No | Page number to return (0-based). Defaults to 0 (the first page). |
| pageSize | integer | No | Maximum number of CSS rules to return per page. Defaults to 10. |
| uid | string | Yes | The uid of the element on the page from the page content snapshot to inspect CSS styles for |

**Example:**
```bash
python3 scripts/call-tool.py get_css_styles '{"pageId":0,"pageIdx":0,"pageSize":0,"uid":"..."}'
```

---

### get_network_request

Gets a network request by an optional reqid, if omitted returns the currently selected request in the DevTools Network panel. Useful for inspecting request headers (including 'Cookie') and response headers (including 'Set-Cookie' and directives).

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| pageId | number | Yes | Targets a specific page by ID. |
| reqid | number | No | The reqid of the network request. If omitted returns the currently selected request in the DevTools Network panel. |
| requestFilePath | string | No | The absolute or relative path to a .network-request file to save the request body to. If omitted, the body is returned inline. |
| responseFilePath | string | No | The absolute or relative path to a .network-response file to save the response body to. If omitted, the body is returned inline. |

**Example:**
```bash
python3 scripts/call-tool.py get_network_request '{"pageId":0,"reqid":0,"requestFilePath":"...","responseFilePath":"..."}'
```

---

### handle_dialog

If a browser dialog was opened, use this command to handle it

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| action | string | Yes | Whether to dismiss or accept the dialog |
| pageId | number | Yes | Targets a specific page by ID. |
| promptText | string | No | Optional prompt text to enter into the dialog. |

**Example:**
```bash
python3 scripts/call-tool.py handle_dialog '{"action":"...","pageId":0,"promptText":"..."}'
```

---

### hover

Hover over the provided element

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| includeSnapshot | boolean | No | Whether to include a snapshot in the response. Default is false. |
| pageId | number | Yes | Targets a specific page by ID. |
| uid | string | Yes | The uid of an element on the page from the page content snapshot |

**Example:**
```bash
python3 scripts/call-tool.py hover '{"includeSnapshot":true,"pageId":0,"uid":"..."}'
```

---

### lighthouse_audit

Get Lighthouse score and reports for accessibility, SEO, best practices, and agentic browsing. This excludes performance. For performance audits, run performance_start_trace

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| device | string | No | Device to emulate. |
| mode | string | No | "navigation" reloads & audits. "snapshot" analyzes current state. |
| outputDirPath | string | No | Directory for reports. If omitted, uses temporary files. |
| pageId | number | Yes | Targets a specific page by ID. |

**Example:**
```bash
python3 scripts/call-tool.py lighthouse_audit '{"device":"...","mode":"...","outputDirPath":"...","pageId":0}'
```

---

### list_console_messages

List all console messages for the target page since the last navigation.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| includePreservedMessages | boolean | No | Set to true to return the preserved messages over the last 3 navigations. |
| includeStackTraces | boolean | No | Set to true to include the stack trace for each message when available. Increases the response size. |
| pageId | number | Yes | Targets a specific page by ID. |
| pageIdx | integer | No | Page number to return (0-based). When omitted, returns the first page. |
| pageSize | integer | No | Maximum number of messages to return. When omitted, returns all messages. |
| serviceWorkerId | string | No | Filter messages to only return messages of the specified service worker. |
| types | array<string> | No | Filter messages to only return messages of the specified resource types. When omitted or empty, returns all messages. |

**Example:**
```bash
python3 scripts/call-tool.py list_console_messages '{"includePreservedMessages":true,"includeStackTraces":true,"pageId":0,"pageIdx":0,"pageSize":0,"serviceWorkerId":"...","types":[]}'
```

---

### list_network_requests

Lists the most recent requests for the target page since the last navigation.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| includePreservedRequests | boolean | No | Set to true to return the preserved requests over the last 3 navigations. |
| pageId | number | Yes | Targets a specific page by ID. |
| pageIdx | integer | No | Page number to return (0-based). When omitted, returns the first page. |
| pageSize | integer | No | Maximum number of requests to return. When omitted, returns all requests. |
| resourceTypes | array<string> | No | Filter requests to only return requests of the specified resource types. When omitted or empty, returns all requests. |

**Example:**
```bash
python3 scripts/call-tool.py list_network_requests '{"includePreservedRequests":true,"pageId":0,"pageIdx":0,"pageSize":0,"resourceTypes":[]}'
```

---

### list_pages

Get a list of pages open in the browser.

No parameters required.

**Example:**
```bash
python3 scripts/call-tool.py list_pages '{}'
```

---

### navigate_page

Go to a URL, or back, forward, or reload. Use project URL if not specified otherwise.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| handleBeforeUnload | string | No | Whether to auto accept or beforeunload dialogs triggered by this navigation. Default is accept. |
| ignoreCache | boolean | No | Whether to ignore cache on reload. |
| initScript | string | No | A JavaScript script to be executed on each new document before any other scripts for the next navigation. |
| pageId | number | Yes | Targets a specific page by ID. |
| timeout | integer | No | Maximum wait time in milliseconds. If set to 0, the default timeout will be used. |
| type | string | No | Navigate the page by URL, back or forward in history, or reload. |
| url | string | No | Target URL (only type=url) |

**Example:**
```bash
python3 scripts/call-tool.py navigate_page '{"handleBeforeUnload":"...","ignoreCache":true,"initScript":"...","pageId":0,"timeout":0,"type":"...","url":"..."}'
```

---

### new_page

Open a new tab and load a URL. Use project URL if not specified otherwise.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| background | boolean | No | Whether to open the page in the background without bringing it to the front. Default is false (foreground). |
| isolatedContext | string | No | If specified, the page is created in an isolated browser context with the given name. Pages in the same browser context share cookies and storage. Pages in different browser contexts are fully isolated (useful for clean-slate testing of cookies and authentication). |
| timeout | integer | No | Maximum wait time in milliseconds. If set to 0, the default timeout will be used. |
| url | string | Yes | URL to load in a new page. |

**Example:**
```bash
python3 scripts/call-tool.py new_page '{"background":true,"isolatedContext":"...","timeout":0,"url":"..."}'
```

---

### performance_analyze_insight

Provides more detailed information on a specific Performance Insight of an insight set that was highlighted in the results of a trace recording.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| insightName | string | Yes | The name of the Insight you want more information on. For example: "DocumentLatency" or "LCPBreakdown" |
| insightSetId | string | Yes | The id for the specific insight set. Only use the ids given in the "Available insight sets" list. |
| pageId | number | Yes | Targets a specific page by ID. |

**Example:**
```bash
python3 scripts/call-tool.py performance_analyze_insight '{"insightName":"...","insightSetId":"...","pageId":0}'
```

---

### performance_start_trace

Start a performance trace on the target webpage. Use to find frontend performance issues, Core Web Vitals (LCP, INP, CLS), and improve page load speed.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| autoStop | boolean | No | Determines if the trace recording should be automatically stopped. |
| filePath | string | No | The absolute file path, or a file path relative to the current working directory, to save the raw trace data. For example, trace.json.gz (compressed) or trace.json (uncompressed). |
| pageId | number | Yes | Targets a specific page by ID. |
| reload | boolean | No | Determines if, once tracing has started, the target page should be automatically reloaded. Navigate the page to the right URL using the navigate_page tool BEFORE starting the trace if reload or autoStop is set to true. |

**Example:**
```bash
python3 scripts/call-tool.py performance_start_trace '{"autoStop":true,"filePath":"...","pageId":0,"reload":true}'
```

---

### performance_stop_trace

Stop the active performance trace recording on the target webpage.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| filePath | string | No | The absolute file path, or a file path relative to the current working directory, to save the raw trace data. For example, trace.json.gz (compressed) or trace.json (uncompressed). |
| pageId | number | Yes | Targets a specific page by ID. |

**Example:**
```bash
python3 scripts/call-tool.py performance_stop_trace '{"filePath":"...","pageId":0}'
```

---

### press_key

Press a key or key combination. Use this when other input methods like fill() cannot be used (e.g., keyboard shortcuts, navigation keys, or special key combinations).

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| includeSnapshot | boolean | No | Whether to include a snapshot in the response. Default is false. |
| key | string | Yes | A key or a combination (e.g., "Enter", "Control+A", "Control++", "Control+Shift+R"). Modifiers: Control, Shift, Alt, Meta |
| pageId | number | Yes | Targets a specific page by ID. |

**Example:**
```bash
python3 scripts/call-tool.py press_key '{"includeSnapshot":true,"key":"...","pageId":0}'
```

---

### resize_page

Resizes the page's window so that the page has specified dimension

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| height | number | Yes | Page height |
| pageId | number | Yes | Targets a specific page by ID. |
| width | number | Yes | Page width |

**Example:**
```bash
python3 scripts/call-tool.py resize_page '{"height":0,"pageId":0,"width":0}'
```

---

### select_page

Select a page as a context for future tool calls.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| bringToFront | boolean | No | Whether to focus the page and bring it to the top. |
| pageId | number | Yes | The ID of the page to select. Call list_pages to get available pages. |

**Example:**
```bash
python3 scripts/call-tool.py select_page '{"bringToFront":true,"pageId":0}'
```

---

### take_heapsnapshot

Capture a heap snapshot of the target page. Use to analyze the memory distribution of JavaScript objects and debug memory leaks.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| filePath | string | Yes | A path to a .heapsnapshot file to save the heapsnapshot to. |
| pageId | number | Yes | Targets a specific page by ID. |

**Example:**
```bash
python3 scripts/call-tool.py take_heapsnapshot '{"filePath":"...","pageId":0}'
```

---

### take_screenshot

Take a screenshot of the page or element.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| filePath | string | No | The absolute path, or a path relative to the current working directory, to save the screenshot to instead of attaching it to the response. |
| format | string | No | Type of format to save the screenshot as. Default is "png" |
| fullPage | boolean | No | If set to true takes a screenshot of the full page instead of the currently visible viewport. Incompatible with uid. |
| pageId | number | Yes | Targets a specific page by ID. |
| quality | number | No | Compression quality for JPEG and WebP formats (0-100). Higher values mean better quality but larger file sizes. Ignored for PNG format. |
| uid | string | No | The uid of an element on the page from the page content snapshot. If omitted, takes a page screenshot. |

**Example:**
```bash
python3 scripts/call-tool.py take_screenshot '{"filePath":"...","format":"...","fullPage":true,"pageId":0,"quality":0,"uid":"..."}'
```

---

### take_snapshot

Take a text snapshot of the target page based on the a11y tree. The snapshot lists page elements along with a unique
identifier (uid). Always use the latest snapshot. Prefer taking a snapshot over taking a screenshot. The snapshot indicates the element selected
in the DevTools Elements panel (if any).

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| filePath | string | No | The absolute path, or a path relative to the current working directory, to save the snapshot to instead of attaching it to the response. |
| pageId | number | Yes | Targets a specific page by ID. |
| verbose | boolean | No | Whether to include all possible information available in the full a11y tree. Default is false. |

**Example:**
```bash
python3 scripts/call-tool.py take_snapshot '{"filePath":"...","pageId":0,"verbose":true}'
```

---

### type_text

Type text using keyboard into a previously focused input

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| pageId | number | Yes | Targets a specific page by ID. |
| submitKey | string | No | Optional key to press after typing. E.g., "Enter", "Tab", "Escape" |
| text | string | Yes | The text to type |

**Example:**
```bash
python3 scripts/call-tool.py type_text '{"pageId":0,"submitKey":"...","text":"..."}'
```

---

### upload_file

Upload a file through a provided element.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| filePaths | array<string> | Yes | One or more files paths to upload. File paths have to be local to the browser instance (not the MCP). |
| includeSnapshot | boolean | No | Whether to include a snapshot in the response. Default is false. |
| pageId | number | Yes | Targets a specific page by ID. |
| uid | string | Yes | The uid of the file input element or an element that will open file chooser on the page from the page content snapshot |

**Example:**
```bash
python3 scripts/call-tool.py upload_file '{"filePaths":[],"includeSnapshot":true,"pageId":0,"uid":"..."}'
```

---

### wait_for

Wait for the specified text to appear on the selected page.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| pageId | number | Yes | Targets a specific page by ID. |
| text | array<string> | Yes | Non-empty list of texts. Resolves when any value appears on the page. |
| timeout | integer | No | Maximum wait time in milliseconds. If set to 0, the default timeout will be used. |

**Example:**
```bash
python3 scripts/call-tool.py wait_for '{"pageId":0,"text":[],"timeout":0}'
```

---

