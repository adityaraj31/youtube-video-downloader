const path = require('path');

module.exports = {
  // ... existing configuration ...
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src'),
    },
    extensions: ['.js', '.jsx', '.json'], // Add other extensions if needed
  },
}; 