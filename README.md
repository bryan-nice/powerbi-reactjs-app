# powerbi-reactjs-app

# react-powerbi
Power BI for React JS which provides components and services to enabling developers to easily embed Power BI reports into their applications.

## Getting started

Install

```bash
npm install --save react-powerbi
```

Include

```javascript
import { Report } from 'react-powerbi';
```

Render component

```jsx
<Report 
  id={this.state.embedConfig.id}
  embedUrl={this.state.embedConfig.embedUrl}
  accessToken={this.state.embedConfig.accessToken}
  filterPaneEnabled={true}
  navContentPaneEnabled={false}
  onEmbedded={this.onEmbedded}
/>
```

## Example
```javascript
import React, { Component } from 'react';
import { Report } from 'react-powerbi';

export default class extends Component {
  onEmbedded(embed) {
    console.log(`Report embedded: `, embed, this);
  }

  render() {
    return (
      <div>
        <h1>react-powerbi demo</h1>

        <Report
          id={this.state.embedConfig.id}
          embedUrl={this.state.embedConfig.embedUrl}
          accessToken={this.state.embedConfig.accessToken}
          filterPaneEnabled={true}
          navContentPaneEnabled={false}
          onEmbedded={this.onEmbedded}
        />
      </div>
    );
  }
}
```

## License

This code is open source and anyone is allowed to use, re-purpose, or modify as long as it conforms to the licenses. The code in this repo is allowed to be in any open source commercial software. No private or public entity is allowed to create nor claim intellectual property if any or all of this code is within their systems. For more details see the [LICENSE](LICENSE).

## Code Origin References:
- Microsoft, 2016, PowerBI-React, GitHub repository, https://github.com/microsoft/PowerBI-React.git, Commit Id: f63823e7a494d73b6793413aed00d2ce92ed4826