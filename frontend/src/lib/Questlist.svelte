<script>
	import { createEventDispatcher } from 'svelte';

	export let quests = [];

	const dispatch = createEventDispatcher();
</script>

<div class="questlist">
	{#each quests as quest}
		<div class="card" on:click={() => dispatch('click', { name: quest.name, quests })}>
			<div class="card-header">
				<h3>{quest.title}</h3>
			</div>

			<div class="card-body">
				<p>{quest.description}</p>
			</div>
			<div class="card-footer">
				<p>Reward: {quest.reward}</p>
			</div>
		</div>
	{/each}
</div>
