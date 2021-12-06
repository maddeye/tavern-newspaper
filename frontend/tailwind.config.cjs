const config = {
	mode: 'jit',
	purge: ['./src/**/*.{html,js,svelte,ts,css,postcss}'],

	theme: {
		extend: {
			backgroundColor: {
				secondary: '#DE127E'
			}
		}
	},

	plugins: []
};

module.exports = config;
