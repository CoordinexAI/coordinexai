from uagents import Agent, Context
from agents.utils import read_json, write_json, DATA_DIR

SNAPSHOT_PATH = DATA_DIR / 'raw' / 'snapshot.json'

agent = Agent(name='ingestor_agent', port=8011)


@agent.on_interval(period=30.0)
async def produce_snapshot(ctx: Context) -> None:
    snapshot = {"slack_msgs": 120, "jira_tickets": 45, "meet_minutes": 820}
    write_json(SNAPSHOT_PATH, snapshot)
    ctx.logger.info('Wrote stub snapshot.')


if __name__ == '__main__':
    agent.run()
