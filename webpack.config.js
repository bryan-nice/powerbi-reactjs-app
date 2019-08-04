module.exports = {
  entry: {
    'react-powerbi': './src/react-powerbi.ts',
  },
  output: {
    path: __dirname + "/dist",
    filename: '[name].js',
    library: 'react-powerbi',
    libraryTarget: 'umd'
  },
  externals: {
    "powerbi-client": "powerbi-client",
    "react": "react"
  },
  devtool: 'source-map',
  resolve: {
    extensions: ['', '.webpack.js', '.web.js', '.ts', '.js']
  },
  module: {
    loaders: [
      { test: /\.map$/, loader: 'ignore-loader' },
      { test: /\.d.ts$/, loader: 'ignore-loader' },
      { test: /\.tsx?$/, exclude: /\.d.ts$/, loader: 'ts-loader' },
      { test: /\.json$/, loader: 'json-loader' }
    ]
  }
};