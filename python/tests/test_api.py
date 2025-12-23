# -*- coding: utf-8 -*-
# @Time    : 2025/03/01

import json
import mcp_marketplace as mcpm

def run_setup_config_deepnlp():

    mcpm.set_endpoint("deepnlp")
    # params = {"query": "map", "page_id":"0", "count_per_page":"20", "mode": "dict"}
    # result = mcpm.search(**params)
    result = mcpm.search(query="map", page_id=0, count_per_page=20, mode="dict")
    print ("DEBUG: run_setup_config_deepnlp result:")
    print (result)

def run_setup_config_pulsemcp():
    """
        https://www.pulsemcp.com/api
        query   
        count_per_page
        offset
    """
    mcpm.set_endpoint("pulsemcp")
    # params = {"query":"Map", "count_per_page":"20", "offset":"0"}
    result = mcpm.search(query="map", count_per_page=20, offset=0)
    print ("DEBUG: run_setup_config_pulsemcp result:")
    print (result)

def run_api_methods():

    """
    """
    ## list
    ## create
    ## delete
    ## 
    ### create
    run_setup_config_pulsemcp()

def run_mcp_router_api_example():
    """
        # 1. This Function Connects to Google-Maps MCPs and run maps_direction from 'Boston' to 'New York'
        # 2. Complete List of Supported Tools Use Check : https://www.deepnlp.org/doc/onekey_mcp_router
    """
    from mcp_marketplace import OneKeyMCPRouter

    example = {"server_name":"google-maps","tool_name":"maps_directions","tool_input":{"destination":"New York","mode":"driving","origin":"Boston"}}
    server_name = example.get("server_name", "")

    ## 1. MCP Initialize POST Request
    ONEKEY_BETA = "BETA_TEST_KEY_OCT_2025"
    router = OneKeyMCPRouter(server_name=server_name, onekey=ONEKEY_BETA)

    ## 2. Check Available Tools, tools/list
    available_tools = router.tools_list(server_name)
    print (f"Server {server_name}|available_tools {available_tools}")

    ## Your LLM Code

    ## 3. Run Tool, Post tools/call request
    result_json = router.tools_call(server_name, example.get("tool_name", ""), example.get("tool_input", {}))
    print (f"Server {server_name}|tool_name {example.get("tool_name", "")} | tool_input {example.get("tool_input", {})} |result_json {result_json}")

def run_mcp_router_batch_api():
    """
    """
    from mcp_marketplace import OneKeyMCPRouter
    ## in the init router function, check if
    # 1. check if DEEPNLP_ONEKEY_ROUTER_ACCESS is set:  DEEPNLP_ONEKEY_ROUTER_ACCESS=BETA_TEST_KEY_OCT_2025
    # 2. Initilialze and post/mcp init method

    import time
    data_examples = [
        {"server_name":"google-maps","tool_name":"maps_directions","tool_input":{"destination":"北京","mode":"driving","origin":"杭州"}},
        {"server_name":"perplexity","tool_name":"perplexity_search","tool_input":{"query":"NBA News","max_results":10,"max_tokens_per_page":256,"country":"US"}}
    ]

    ONEKEY_BETA = "BETA_TEST_KEY_OCT_2025"
    mcp_routers_dict = {}
    for data_example in data_examples:
        server_name = data_example.get("server_name", "")
        mcp_routers_dict[server_name] = OneKeyMCPRouter(server_name=server_name, onekey = ONEKEY_BETA)
        # mcp_routers_dict[server_name] = OneKeyMCPRouter(server_name=server_name, onekey = ONEKEY_BETA, log_enable=True)
        print (f"INFO: OneKey MCP Router Initialize Server Connection|{server_name} ")

    for i in range(len(data_examples)):
        data_example = data_examples[i]
        server_name = data_example.get("server_name", "")
        router = mcp_routers_dict.get(server_name)
        if router is None:
            print (f"DEBUG: server_name {server_name} is None...")
        ## 1. tools/list
        available_tools = router.tools_list(server_name)
        print (f"INFO: server_name {server_name} available tools: {available_tools}")

        ## 2. Your LLM Function Call choose tools and fill function call arguments

        ## 3. Your MCP
        tool_name = data_example.get("tool_name", "")
        tool_input = data_example.get("tool_input", {})
        ## tools/call
        result_json = router.tools_call(server_name, tool_name, tool_input)
        print(f"INFO: Server Name {server_name} | Tool Name {tool_name} | Tool Call Result {result_json}")
        ## $.result.success, $.result.content
        success = result_json.get("result", {}).get("success")
        content_list = result_json.get("result", {}).get("content")
        for content in content_list:
            print (f"Content Type {content.get('type')}")
            print (f"Content Text {content.get('text')}")

        time.sleep(1)

"""
INFO: server_name google-maps available tools: {'result': {'tools': [{'name': 'maps_geocode', 'description': 'Convert an address into geographic coordinates', 'inputSchema': {'type': 'object', 'properties': {'address': {'type': 'string', 'description': 'The address to geocode'}}, 'required': ['address']}}, {'name': 'maps_reverse_geocode', 'description': 'Convert coordinates into an address', 'inputSchema': {'type': 'object', 'properties': {'latitude': {'type': 'number', 'description': 'Latitude coordinate'}, 'longitude': {'type': 'number', 'description': 'Longitude coordinate'}}, 'required': ['latitude', 'longitude']}}, {'name': 'maps_search_places', 'description': 'Search for places using Google Places API', 'inputSchema': {'type': 'object', 'properties': {'query': {'type': 'string', 'description': 'Search query'}, 'location': {'type': 'object', 'properties': {'latitude': {'type': 'number'}, 'longitude': {'type': 'number'}}, 'description': 'Optional center point for the search'}, 'radius': {'type': 'number', 'description': 'Search radius in meters (max 50000)'}}, 'required': ['query']}}, {'name': 'maps_place_details', 'description': 'Get detailed information about a specific place', 'inputSchema': {'type': 'object', 'properties': {'place_id': {'type': 'string', 'description': 'The place ID to get details for'}}, 'required': ['place_id']}}, {'name': 'maps_distance_matrix', 'description': 'Calculate travel distance and time for multiple origins and destinations', 'inputSchema': {'type': 'object', 'properties': {'origins': {'type': 'array', 'items': {'type': 'string'}, 'description': 'Array of origin addresses or coordinates'}, 'destinations': {'type': 'array', 'items': {'type': 'string'}, 'description': 'Array of destination addresses or coordinates'}, 'mode': {'type': 'string', 'description': 'Travel mode (driving, walking, bicycling, transit)', 'enum': ['driving', 'walking', 'bicycling', 'transit']}}, 'required': ['origins', 'destinations']}}, {'name': 'maps_elevation', 'description': 'Get elevation data for locations on the earth', 'inputSchema': {'type': 'object', 'properties': {'locations': {'type': 'array', 'items': {'type': 'object', 'properties': {'latitude': {'type': 'number'}, 'longitude': {'type': 'number'}}, 'required': ['latitude', 'longitude']}, 'description': 'Array of locations to get elevation for'}}, 'required': ['locations']}}, {'name': 'maps_directions', 'description': 'Get directions between two points', 'inputSchema': {'type': 'object', 'properties': {'origin': {'type': 'string', 'description': 'Starting point address or coordinates'}, 'destination': {'type': 'string', 'description': 'Ending point address or coordinates'}, 'mode': {'type': 'string', 'description': 'Travel mode (driving, walking, bicycling, transit)', 'enum': ['driving', 'walking', 'bicycling', 'transit']}}, 'required': ['origin', 'destination']}}]}, 'jsonrpc': '2.0', 'id': '2'}
INFO: Server Name google-maps | Tool Name maps_directions | Tool Call Result {'jsonrpc': '2.0', 'result': {'success': True, 'content': [{'type': 'text', 'text': '{\n  "routes": [\n    {\n      "summary": "京沪高速公路/G2",\n      "distance": {\n        "text": "1,272 km",\n        "value": 1272406\n      },\n      "duration": {\n        "text": "12 hours 34 mins",\n        "value": 45224\n      },\n      "steps": [\n        {\n          "instructions": "Head <b>north</b> on <b>莫干山路</b> toward <b>密渡桥路</b>",\n          "distance": {\n            "text": "55 m",\n            "value": 55\n          },\n          "duration": {\n            "text": "1 min",\n            "value": 10\n          },\n          "travel_mode": "DRIVING"\n        },\n        {\n          "instructions": "Turn <b>right</b> onto <b>密渡桥路</b>",\n          "distance": {\n            "text": "0.5 km",\n            "value": 492\n          },\n          "duration": {\n            "text": "2 mins",\n            "value": 127\n          },\n          "travel_mode": "DRIVING"\n        },\n        {\n          "instructions": "Turn <b>right</b> to stay on <b>密渡桥路</b>",\n          "distance": {\n            "text": "0.2 km",\n            "value": 218\n          },\n          "duration": {\n            "text": "1 min",\n            "value": 43\n          },\n          "travel_mode": "DRIVING"\n        },\n        {\n          "instructions": "Turn <b>left</b> onto <b>环城北路</b>",\n          "distance": {\n            "text": "0.7 km",\n            "value": 672\n          },\n          "duration": {\n            "text": "2 mins",\n            "value": 94\n          },\n          "travel_mode": "DRIVING"\n        },\n        {\n          "instructions": "Turn <b>left</b> onto <b>中北桥</b>/<wbr/><b>中山北路</b><div style=\\"font-size:0.9em\\">Continue to follow 中山北路</div>",\n          "distance": {\n            "text": "0.3 km",\n            "value": 312\n          },\n          "duration": {\n            "text": "1 min",\n            "value": 67\n          },\n          "travel_mode": "DRIVING"\n        },\n        {\n          "instructions"

INFO: Server Name perplexity | Tool Name perplexity_search | Tool Call Result {'jsonrpc': '2.0', 'result': {'success': True, 'content': [{'type': 'text', 'text': 'Found 10 search results:\n\n1. **NBA**\n   URL: https://www.espn.com/nba/\n   ## Fast break: Eric Moody on Mikal Bridges\' durability, Kel\'el Ware\'s rise and more\n\nFantasy basketball insights, including Bridges\' durability and production, Ware\'s second-year rise, more.... - NBA veteran Gallinari retires from basketball\n\n- Sources: Pels\' Williamson out at least 3 weeks\n\n- Luka takes blame: \'No way I can have 9 turnovers\'\n\n- Brooks resumes LeBron trash talk in 33-point show\n\n- Nuggets\' Murray sprains ankle in loss to Mavs\n\n- Booker exits Suns\' win vs. Lakers with groin injury\n\n- 👀 Why LeBron\'s most remarkable streak is at risk... ## Inside the Mavericks\' power struggle: Nico Harrison vs. Mark Cuban\n\nHere\'s what led to the end of Nico Harrison\'s tenure with the Dallas Mavericks 11 games into the season, and how Mark Cuban was involved.\n\n## NBA first-month lessons: What we\'re hearing on all 30 teams\n\nTim Bontemps takes the pulse of the league on OKC\'s chase for 70 wins, the potential post-Trae Hawks and more first-month standout storylines.\n   Date: 2025-12-01\n\n2. **NBA News, Scores, Stats, Standings and Rumors**\n   URL: https://www.cbssports.com/nba/\n   As we hit the end of the first quarter in the 2025-26 NBA season, we\'re handing out grades.\n\nOn Black Friday, we\'re taking a look at the biggest bargains in the NBA this season\n\nLet\'s look at some of the big-picture winners and losers of the now-completed group stage\n   Date: 2025-12-02\n\n3. **NBA | NBA News, Scores, Highlights, Stats, Standings, and Rumors | Bleacher Report**\n   URL: https://bleacherreport.com/nba\n   ## Suns Upset Lakers in LA 😱Dillon Brooks and Collin Gillespie combine for 61; LeBron scores 10 to keep his streak alive... ## Bane Tallies 37 in Home Win ♨️Magic top Bulls 125-120 to reach 3rd straight victory\n\n## MPJ Drops 35 Against Hornets 😮💨Nets FINALLY get their first win at home\n\n## Luka Confronts Pels Rookie 😳Jeremiah Fears got into it with Jimmy yesterday, and Dončić today... ## Pritchard Drops 42 on Cavs ☘️Season high in scoring while Jaylen Brown records a triple-double\n\n## Jalen Johnson COOKS 76ers 🪣First-ever 40+ point game leads Hawks to 2OT win vs. Maxey (44 points) Bleacher Report•2d... ## Lakers Win 7 In a Row 📈15-4 through 19 games with a back-to-back on Monday 📲\n\n## Flagg Scores 35 to Send Clippers to 5-15 😳Mavs star rookie and Klay (23 points) dominate to snap Mavs\' 3-game losing streak Bleacher Report•2d\n   Date: 2025-12-03\n\n4. **NBA News, Scores & Expert Analysis | Sports Illustrated**\n   URL: https://www.si.com/nba\n   Two L.A. Stories: Clippers and Lakers Going in Completely Opposite DirectionThe Clippers dropped their fifth straight and it’s unclear how they get out of this spiral. Across town, the Lakers may be a deadline move from competing in the West.\n   Date: 2025-12-02\n\n5. **NBA: Breaking News, Rumors & Highlights - Yardbarker**\n   URL: https://www.yardbarker.com/nba\n   Saturday, Cooper Flagg became the second 18-year-old to ever score 30 points in an NBA game.\n\nGiannis Antetokounmpo already has a legacy that makes him one of the greatest players in NBA history. On Saturday, he further cemented his legendary status by reaching a major career milestone at a historic pace.... Heading into Saturday night, the Toronto Raptors had the NBA\'s second-longest winning streak at nine games.\n\nYoung injured his knee in a collision with teammate Mouhamed Gueye in the first quarter of an Oct. 29 game at Brooklyn.\n\nThe Dallas Mavericks’ No. 1 overall pick Cooper Flagg has often been compared to LeBron James.... Jokic has long been considered one of the best players in the NBA, if not the best.\n\nThe Golden State Warriors are 10-10, just lost Steph Curry and desperately need veteran reinforcements.\n\nDoncic improved to 3-0 against Dallas after his surprising trade from the Mavericks in February.\n\nJalen Brunson scored a game-high 37 points on Friday, helping the New York Knicks earn a 118-109 victory over the visiting Milwaukee Bucks and advance to the NBA Cup knockout stage.\n   Date: 2025-01-01\n\n6. **NBA**\n   URL: https://www.foxsports.com/nba\n   BROWSE BY\n\nSPORTS & TEAMS\n\nPLAYERS\n\nSHOWS\n\nPERSONALITIES\n\nTOPICS\n\nBuilt on\n\nNBA\n\n6 GAMES yesterday\n\n6 GAMES yesterday\n\nNBA\n\n\n\nNBA\n\nFEATURED\n\nFEATURED\n\nSCORES\n\nSCHEDULE\n\nSTANDINGS\n\nSTATS\n\nVIDEOS... FOX SPORTS\n\nThunder blow out Lakers, Is Los Angeles & Luka not a contender? | The Herd\n\nNOVEMBER 13\n\n\n\nFOX SPORTS\n\nWhy Nick believes Ravens\' \'season if over \' if they lose to the Vikings, Bills STILL contenders? 🤔\n\nNOVEMBER 7\n\n\n\nFOX SPORTS\n\nNick says Luka Doncic is ‘reminding everyone who he is’, Can the Broncos win the AFC West? | FTF... NOVEMBER 6\n\n\n\nFOX SPORTS\n\nLuka Doncic scores 35 in Lakers win over Spurs, Is Los Angeles a title contender? | The Herd\n\nNOVEMBER 6\n\n\n\nFOX SPORTS\n\nAustin Reaves leads Lakers to win, How far can the big 3 of LeBron, Luka, and Reaves go? | The Herd\n   Date: 2025-12-02\n\n7. **NBA News**\n   URL: https://www.foxsports.com/nba/news\n   ### Celtics hold off late Knicks charge to win 123-117 in rematch of East semifinalJaylen Brown scores a season-high 42 points, leading the Boston Celtics to a 123-117 victory over the New York Knicks in a rematch of last season\'s Eastern Conference semifinal\n\n11 MINS AGO • Associated Press\n   Date: 2025-12-03\n\n8. **NBA quarter-season grades for every West team, from obvious \'A+\' to alarming \'F-\'**\n   URL: https://www.cbssports.com/nba/news/nba-quarter-season-grades-western-conference-lakers-clippers-thunder-rockets-nuggets/\n   (In their last seven games, a stretch in which Gordon played a total of three minutes, they surrendered 122.9 points per 100 possessions)... The Lakers are great at the things they expected to be great at. Luka Dončić and Austin Reaves are currently on pace to become the highest-scoring duo in a single season (on a per-game basis) in post-merger league history, and while LeBron James hasn\'t posted gaudy numbers since returning, he\'s slid in comfortably, done a little bit of everything and injected some badly needed pace into an otherwise slow offense.... Lauri Markkanen has cooled off a bit in the last couple of weeks, but he\'s still averaging a career-high 28 points on 60.6% true shooting. Regardless of whether the Jazz are going to trade him or build around him, this is exactly what they needed from him after a disappointing 2024-25 season. Markkanen is not, however, the Jazzman who has made the biggest leap -- that is clearly George, whose improved decision-making and finishing have made him into a totally different kind of threat with the ball in his hands.\n   Date: 2025-12-02\n\n9. **More NBA News - ESPN**\n   URL: https://www.espn.com/nba/news/more/_/sport/nba\n   **Thunder match Blazers\' $70M offer to Kanter**\n\nThe Thunder took all three possible days, but decided to match the Portland Trail Blazers \' maximum-level $70 million offer sheet for Enes Kanter.\n\n**LeBron: \'Nightmares\' over Finals loss to GSW**\n\nLeBron James says he has \'nightmares\' over certain situations in the Cleveland Cavaliers\' Finals loss to the Golden State Warriors.... **Nets swoop in to sign Bargnani ahead of Kings**\n\nThe Brooklyn Nets have swooped in to sign former No. 1 overall pick Andrea Bargnani, swiping him away at the 11th hour from the Sacramento Kings.\n\n**Bucks, Henson heading toward deal, sources say**... **Marcus Morris: Suns trade a \'slap in the face\'**\n\nMarcus Morris, who was introduced Friday by the Detroit Pistons, said the way his trade from the Phoenix Suns unfolded was a "slap in the face."\n\n**Saunders: Garnett will be starter next season**\n\nMinnesota Timberwolves president and coach Flip Saunders says he plans to start Kevin Garnett next season and believes he can still make a significant impact at age 39.\n   Date: 2011-12-01\n\n10. **NBA Rumors - HoopsRumors.com**\n   URL: https://www.hoopsrumors.com\n   **Suns** forward **Dillon Brooks** relished beating the Lakers in Los Angeles on Monday as well as the opportunity to trash talk **LeBron James**, Tim MacMahon writes for ESPN.com.... As MacMahon notes, Brooks infamously got under James’ skin during the first round of the 2023 playoffs with Memphis, only to see the strategy backfire — he struggled for the rest of the series while James dominated, and the Grizzlies were eliminated in six games. Ever the antagonist, Brooks poured in 33 points on Monday — one off his season-high — and “relentlessly” mocked James and the crowd.... Phoenix cruised to an easy victory on Monday despite missing\n\n**Devin Booker** (right groin injury) for the majority of the contest. Brooks was the driving force behind the result.\n\n\n\n*Sometimes, I’m trying to tell him to chill out, but I think he just blacks out*,” said point guard **Collin Gillespie**, who scored a career-high 28 points on Monday and whom Brooks has nicknamed “Villain Jr.” due to his tenacity. “ *That’s Dillon Brooks. It fuels us. Obviously, we love when he gets going.*\n   Date: 2025-12-02\n\n'}]}, 'id': '3'}
Content Type text
Content Text Found 10 search results:

1. **NBA**
   URL: https://www.espn.com/nba/
   ## Fast break: Eric Moody on Mikal Bridges' durability, Kel'el Ware's rise and more
Fantasy basketball insights, including Bridges' durability and production, Ware's second-year rise, more.... - NBA veteran Gallinari retires from basketball
"""

def main():

    run_setup_config_pulsemcp()

    run_setup_config_deepnlp()


if __name__ == '__main__':
    main()
