const { defineConfig } = require('@vue/cli-service')
// module.exports = defineConfig({
//   transpileDependencies: true,
// })
module.exports = {
  // Otras configuraciones
  publicPath: process.env.NODE_ENV === 'production' ? './' : '/',
};