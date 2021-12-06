<script>
	import { getData } from '$lib/fetch.js';

	import LoadingSpinner from '$lib/LoadingSpinner.svelte';
	import Questlist from '$lib/Questlist.svelte';

	const baserUrl = import.meta.env.VITE_APP_BACKEND_URL;

	console.log(baserUrl);

	let response = getData(`${baserUrl}quests/3`);

	async function test() {
		console.log(await fetch('http://localhost:8000/api/quests/3'));
	}

	function sleep(ms) {
		return new Promise((resolve) => setTimeout(resolve, ms));
	}

	const selectQuest = async ({ detail }) => {
		await fetch(`${baserUrl}done/${detail.name}`);

		detail.quests.forEach(async (q) => {
			console.log(q.name, detail.name);
			if (q.name != detail.name) {
				await fetch(`${baserUrl}escalate/${q.name}`);
			}
		});

		await sleep(200);

		response = getData(`${baserUrl}quests/3`);
	};

	const advanceDay = async (evt) => {
		response = getData(`${baserUrl}advance/3`);
	};

	test();
</script>

<h2 class="headline">Select a quest:</h2>

{#await $response}
	<div class="loader">
		<LoadingSpinner />
	</div>
{:then data}
	<Questlist quests={data} on:click={selectQuest} />

	<div class="controls">
		<button on:click={advanceDay}>Advance 1 Day</button>
	</div>
{:catch error}
	<p>There went something wrong.</p>
	<p>{error.message}</p>
{/await}
