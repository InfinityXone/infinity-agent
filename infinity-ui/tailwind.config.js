/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,ts,jsx,tsx}"
  ],
  theme: {
    extend: {
      colors: {
        offblack: "#0b0b0b",
        neonblue: "#00e5ff",
        silver: "#b0b0b0",
        glass: "rgba(0,0,0,0.7)",
      },
      fontFamily: {
        modern: ['"Inter"', "sans-serif"],
      },
    },
  },
  plugins: [],
};
