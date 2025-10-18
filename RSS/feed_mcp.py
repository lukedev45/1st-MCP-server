from fastmcp import FastMCP
import feedparser

mcp = FastMCP(name = 'Quantum RSS Feed Reader')

@mcp.tool()
def quantum_news_rss_feed(query: str, max_results: int = 5):
    """Search Quantum Insider RSS feed for news articles related to the query."""
    feed = feedparser.parse("https://thequantuminsider.com/rss")
    results = []
    query_lower = query.lower()
    for entry in feed.entries:
        title = entry.get("title", "")
        description = entry.get("description", "")
        if query_lower in title.lower() or query_lower in description.lower():
            results.append({
                "title": title,
                "url": entry.get("link", ""),
                "published": entry.get("published", ""),
            })
        if len(results) >= max_results:
            break

    return results or [{"message": "No reults found."}]

@mcp.tool()
def qiskit_youtube_rss_feed(query: str, max_results: int = 5):
    """Search Qiskit YouTube channel RSS feed for videos related to the query."""
    feed = feedparser.parse("https://www.youtube.com/feeds/videos.xml?channel_id=UClBNq7mCMf5xm8baE_VMl3A")
    results = []
    query_lower = query.lower()
    for entry in feed.entries:
        title = entry.get("title", "")
        if query_lower in title.lower():
            results.append({
                "title": title,
                "url": entry.get("link", ""),
            })
        if len(results) >= max_results:
            break
    return results or [{"message": "No results found."}]

if __name__ == "__main__":
    mcp.run(transport="http")  # STDIO by default
