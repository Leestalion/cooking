const tailwindcss = require('tailwindcss')
const defaultTheme = require('tailwindcss/defaultTheme')

module.exports = {
  future: {
    // re;oveDeprecatedGapUtilities: true,
    // purgeLayersByDefault: true,
  },
  purge: [],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter var', ...defaultTheme.fontFamily.sans],
      },
    },
  },
  variants: {},
  plugins: [],
}
