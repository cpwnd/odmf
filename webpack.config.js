const path = require('path');

module.exports = {
  entry: './node_modules/jquery/dist/jquery.min.js',
  target: 'web',
  mode: 'development',
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'src/webpage/media/dist')
  }
};
