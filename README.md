<<<<<<< HEAD
# powerbi-reactjs-app
=======
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

>>>>>>> PowerBI-React/master
