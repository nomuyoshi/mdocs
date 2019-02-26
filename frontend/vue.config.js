const BundleTracker = require('webpack-bundle-tracker');
const webpack = require('webpack'); // eslint-disable-line import/no-extraneous-dependencies

module.exports = {
  publicPath: 'http://127.0.0.1:8080/',
  outputDir: './dist/',
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
  },
};
