module.exports = {
    extends: 'google',
    quotes: [2, 'single'],
    globals: {
        SwaggerEditor: false
    },
    env: {
        browser: true
    },
    rules:{
        "linebreak-style": 0,
        "eol-last": 0,
        "no-multiple-empty-lines": ["error", { "max": 1, "maxEOF": 0 }],
    }
};