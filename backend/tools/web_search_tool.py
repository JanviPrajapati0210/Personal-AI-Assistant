from duckduckgo_search import DDGS


def web_search(query):

    results = []

    with DDGS() as ddgs:

        search_results = ddgs.text(
            query,
            max_results=3
        )

        for result in search_results:

            results.append(
                result["body"]
            )

    return "\n".join(results)