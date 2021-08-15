const defaultTheme = require('tailwindcss/defaultTheme')
const colors = require('tailwindcss/colors')

module.exports = {
    mode: 'jit',
    purge: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
    darkMode: 'class', // or 'media' or 'class'
    theme: {
        extend: {
            colors: {
                // transparent: 'transparent',
                // current: 'currentColor',
                // black: colors.black,
                // white: colors.white,
                // gray: colors.coolGray,
                // trueGray: colors.trueGray,
                // indigo: colors.indigo,
                // purple: colors.purple,
                // violet: colors.violet,
                // red: colors.red,
                // pink: colors.pink,
                // rose: colors.rose,
                // yellow: colors.yellow,
                // amber: colors.amber,
                // green: colors.green,
            },
            screens: {
                'tablet': '640px',
                'laptop': '1024px',
                'desktop': '1280px',
            },
            fontFamily: {
                sans: ['Inter var', ...defaultTheme.fontFamily.sans],
            },
        },
    },
    variants: {
        extend: {},
    },
    plugins: [
        require('@tailwindcss/forms'),
    ],
}
