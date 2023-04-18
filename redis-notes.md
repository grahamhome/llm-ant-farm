# Redis as Database notes
# Process:
- Install redis-om
- Define Memory model with Pydantic as [seen here](https://github.com/redis/redis-om-python/blob/main/docs/getting_started.md)
    - Content
    - Agent name 
- Create migration script to add index on vector field, agent name field, access date, importance
- Write query to select KNN by vector, filter by agent name, importance and access date
- Done: now we can query Memories for any agent by relevance, importance and recency.