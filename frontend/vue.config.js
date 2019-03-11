const BundleTracker = require('webpack-bundle-tracker');
const webpack = require('webpack'); // eslint-disable-line import/no-extraneous-dependencies
const path = require("path");

module.exports = {
  publicPath: process.env.NODE_ENV === 'development' ? 'http://127.0.0.1:8080/' : '/',
  outputDir: path.resolve(__dirname, '../static/bundles/'),
  pluginOptions: {
    "style-resources-loader": {
      preProcessor: "scss",
      patterns: [path.resolve(__dirname, './src/assets/application.scss')]
    }
  },
  chainWebpack: (config) => {
    config.optimization.splitChunks(false);
    config.plugin('BundleTracker').use(BundleTracker, [{ filename: './webpack-stats.json' }]);
    config.resolve.alias.set('__STATIC__', 'static');
    config.devServer
      .public('http://127.0.0.1:8080')
      .hotOnly(true)
      .watchOptions({ poll: 1000 })
      .https(false);
  },
  configureWebpack: {
    plugins: [
      new webpack.ContextReplacementPlugin(/moment[/]locale$/, /ja/),
    ],
    devServer: {
      watchOptions: {
        poll: true
      }
    }
  },
};
