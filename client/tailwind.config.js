module.exports = {
  content: [
    "./public/**/*.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        'title': ['Amatic SC', 'cursive'],
      },
      colors: {
        'm-orange': {
          50: '#fff1ea',
          100: '#ffe3d4',
          200: '#ffc6a9',
          300: '#ffaa7f',
          400: '#ff8d54',
          500: '#ff7129',
          600: '#cc5a21',
          700: '#994419',
          800: '#662d10',
          900: '#331708',
        },
        'm-grey': {
          50: '#eaeaea',
          100: '#d5d5d5',
          200: '#acacaa',
          300: '#828280',
          400: '#595955',
          500: '#2f2f2b',
          600: '#262622',
          700: '#1c1c1a',
          800: '#131311',
          900: '#090909',
        }
      },
    },
  },
  plugins: [],
}
