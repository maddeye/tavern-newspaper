# Tavern Newspaper

Tiny helper to create and manage quests to make your world feel alive.
(Made for a friend!)

## Usage

Copy and modify the json files within the backend/quests folder.

Title: Title of the quest
Description: Description of the quest
City: Needed city escalation level for the quest to appear
Escalation: Escalation level of the quest needed to appear
Reward: Quest reward

After you finished your quests run

```bash
$ docker-compose -f docker-compose.yml up -d
```

and navigate to http://localhost:8080

Have Fun!

### Tech Stack

- :snake: Python + FastApi
- SvelteKit
- :whale: Docker + Docker-Compose
