

def example_onekey_mcp_google_map():
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

def example_onekey_mcp_gaode_map():
    """
        # 1. This Function Connects to Google-Maps MCPs and run maps_direction from 'Boston' to 'New York'
        # 2. Complete List of Supported Tools Use Check : https://www.deepnlp.org/doc/onekey_mcp_router
    """
    from mcp_marketplace import OneKeyMCPRouter

    example = {"server_id":"amap-maps-streamableHTTP","tool_name":"maps_geo","tool_input":{'address': '杭州东站', 'city': ''}}
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



def example_onekey_mcp_baidu_map():
    """
        Example of Using DeepNLP OneKey MCP Router to Access Commercial MCPs
    """
    from mcp_marketplace import OneKeyMCPRouter

    example = {"server_id":"baidu-maps-sse",
               "tool_name":"map_search_places",
               "tool_input":{"query":"中关村","tag":"西餐","region":"北京","location":"39.97,116.31","radius":3000,"language":"zh","is_china":"true"}}
    server_name = example.get("server_name", "")

    ## 1. MCP Initialize POST Request
    ONEKEY_BETA = "BETA_TEST_KEY_OCT_2025"
    router = OneKeyMCPRouter(server_name=server_name, onekey=ONEKEY_BETA)

    ## 2. Check Available Tools, tools/list
    available_tools = router.tools_list(server_name)
    print(f"Server {server_name}|available_tools {available_tools}")

    ## Your LLM Code

    ## 3. Run Tool, Post tools/call request
    result_json = router.tools_call(server_name, example.get("tool_name", ""), example.get("tool_input", {}))
    print(
        f"Server {server_name}|tool_name {example.get("tool_name", "")} | tool_input {example.get("tool_input", {})} |result_json {result_json}")


def example_onekey_mcp_perplexity_search_reason():
    """
        {"server_id":"perplexity","tool_name":"perplexity_search","tool_input":{"query":"NBA News","max_results":10,"max_tokens_per_page":256,"country":"US"}}
    """
    from mcp_marketplace import OneKeyMCPRouter

    function_call_data_example = {"server_name":"perplexity","tool_name":"perplexity_search","tool_input":{"query":"NBA News","max_results":10,"max_tokens_per_page":256,"country":"US"}}

    server_name = function_call_data_example.get("server_name", "")

    ## 1. MCP Initialize POST Request
    ONEKEY_BETA = "BETA_TEST_KEY_OCT_2025"
    router = OneKeyMCPRouter(server_name=server_name, onekey=ONEKEY_BETA)

    ## 2. Check Available Tools, tools/list
    available_tools = router.tools_list(server_name)
    print(f"Server {server_name}|available_tools {available_tools}")

    ## Your LLM Code

    ## 3. Run Tool, Post tools/call request
    result_json = router.tools_call(server_name, function_call_data_example.get("tool_name", ""), function_call_data_example.get("tool_input", {}))
    print(
        f"Server {server_name}|tool_name {function_call_data_example.get("tool_name", "")} | tool_input {function_call_data_example.get("tool_input", {})} |result_json {result_json}")

    """
    Server perplexity|tool_name perplexity_search | tool_input {'query': 'NBA News', 'max_results': 10, 'max_tokens_per_page': 256, 'country': 'US'} |result_json {'jsonrpc': '2.0', 'result': {'success': True, 'content': [{'type': 'text', 'text': 'Found 10 search results:\n\n1. **NBA on ESPN - Scores, Stats and Highlights**\n   URL: https://www.espn.com/nba/\n   ## Customize ESPN\n\n## Live updates as Lakers host Spurs; Thunder on to Las Vegas\n\nThe NBA Cup quarterfinals continue Wednesday night, when the Oklahoma City Thunder square off with the Phoenix Suns and the San Antonio Spurs take on Los Angeles Lakers. Follow along for live updates.\n\n- Curry (thigh) expected to return Fri. vs. Wolves\n\n- Sources: Lakers using regular court in NBA Cup QF\n\n- Mavs\' Lively to have season-ending foot surgery\n\n- Knicks, closer to an identity, reach NBA Cup semis... ## Perk: KAT is most important player on the Knicks\n\n## Highlights, top moments as Knicks, Magic punch tickets to Las Vegas\n\nHere are the key moments from Tuesday\'s NBA Cup quarterfinals as the Knicks and Magic advanced.... - Curry (thigh) expected to return Fri. vs. Wolves\n\n- Sources: Lakers using regular court in NBA Cup QF\n\n- Mavs\' Lively to have season-ending foot surgery\n\n- Knicks, closer to an identity, reach NBA Cup semis\n\n- Bane burns Heat with 37; Magic advance to Vegas\n\n- Spurs rule Wemby out for Cup game vs. Lakers\n\n- 👀 Everything Shams is hearing on trade season\n   Date: 2025-12-09\n\n2. **NBA News, Scores, Stats, Standings and Rumors**\n   URL: https://www.cbssports.com/nba/\n   The Thunder have tied the best 25-game start in NBA history, and the reigning champs are annihilating the competition.\n\nThe Celtics have been one of the NBA\'s biggest overachievers so far this season\n\nGiannis is seemingly on the trade market, but teams are still reportedly being cautious about what they\'d offer\n   Date: 2025-12-11\n\n3. **NBA News, NBA Rumors, Trades, Free Agency - RealGM**\n   URL: https://basketball.realgm.com/nba/news\n   Myles Turner said the Indiana Pacers made his free agency decision easy after offering only $22 million annually over three years. The Milwaukee Bucks presented a four-year, $107 million contract that Turner signed in July.\n\nNegotiations between Turner\'s agent and the Pacers stalled quickly after Indiana reached the NBA Finals in June. The Pacers never extended an offer beyond $66 million over three years.... Pacers president Kevin Pritchard said he learned of Turner\'s decision through social media. He believed negotiations were still ongoing and thought Indiana was near an acceptable number.\n\n"Herb Simon and Steven Rales and the Simon family were fully prepared to go deep into the tax to keep him," Pritchard said in July. "We were negotiating in good faith."... Turner spent 10 seasons with Indiana after being drafted in 2015. He was the longest-tenured player on last season\'s Finals team.\n\n"[Indiana] made it very clear how they valued me," Turner said. "And so did the Milwaukee Bucks."\n\nTurner will face the Pacers for the first time Monday at Gainbridge Fieldhouse. The Bucks are 4-1 while Indiana has started 0-5.\n   Date: 2025-11-03\n\n4. **NBA**\n   URL: https://bleacherreport.com/nba\n   ## Brunson Goes Off vs. Raptors 🔥Knicks star\'s 20-point first quarter overpowers Toronto as New York clinches NBA Cup semis 35 PTS | 3 REB | 4 AST | 13 FGMBleacher Report•10h\n\n## Lakers Not Using NBA Cup CourtLA switching back to normal surface vs. Spurs as precautionary measure (ESPN)... ## Desmond Bane Fined $35KMagic guard penalized for throwing ball at Knicks\' OG Anunoby on SundayBleacher Report•2d\n\n## Blockbuster Harden Trade Idea 💡Cooking up a deal to bolster a Western contender ➡️\n\n## Bane Chucks Ball at Anunoby 😳Magic-Knicks gets heated after this moment... ## Kerr: Cause for Kuminga DNP is PrivateWarriors HC not willing to discuss why JK logged zero minutes vs. BullsBleacher Report•2d\n\n## Warriors to Explore Kuminga TradeProbability of move \'remains strong\' after DNP vs. Bulls (ESPN)\n\n## Celtics Win 5th Straight ☘️Boston leaps Raptors for No. 3 in East standings despite rocky start to season Bleacher Report•3d\n   Date: 2025-12-11\n\n5. **NBA Rumors - HoopsRumors.com**\n   URL: https://www.hoopsrumors.com\n   - Kerr addressed the status of\n\n**Jonathan Kuminga**, who will be become eligible to be traded on January 15 (Twitter video link from Slater). Speculation that Kuminga will be shipped out increased after he received a DNP in Sunday’s game at Chicago. *“I can imagine it’s not easy for him,”*Kerr said. *“We talked about the situation. My desire is for JK to be the best player he can be, regardless of where he ends up, whether it’s here or elsewhere.”*... * **Ariel Hukporti**‘s speed could be his path to an increased role with the **Knicks**, according to Kristian Winfield of The New York Daily News, (subscription required) who notes that head coach **Mike Brown**referred to Hukporti as “one of the fastest bigs I’ve ever been around.” Hukporti, who has had a limited role this fall, logged a season-high 23 minutes in Sunday’s win over Orlando, but played just 73 seconds on Tuesday vs. Toronto and was assigned to the G League on Wednesday (Twitter link).\n   Date: 2025-12-11\n\n6. **NBA: Breaking News, Rumors & Highlights**\n   URL: https://www.yardbarker.com/nba\n   New York Knicks point guard Jalen Brunson delivered 35 points Tuesday night in Toronto to send his team into uncharted territory.\n\nThe Lakers are tied with the Denver Nuggets with a 17-6 record and are sitting in second place in the stacked Western Conference.\n\nHow many of the active NBA players to make six three-pointers in a single game on at least 15 occasions in their career can you name in eight minutes?... Heat guard Terry Rozier pleaded not guilty to two federal charges related to illegal sports betting on Monday in Brooklyn federal court, reports Mike Vorkunov of The Athletic.\n\nKuminga will become eligible to be traded on Dec. 15.\n\nBasketball is a team game, but it\'s also a sport that judges its players by how much their wins more than any other.... The Golden State Warriors wrapped up a 2-1 road trip without the injured Steph Curry and Draymond Green. In Sunday\'s 123-91 shellacking of the Chicago Bulls, they also played without the healthy Jonathan Kuminga.\n\nJames Harden doesn\'t often come to mind when listing the top players in NBA history. But there is one thing you can\'t doubt about Harden: The man can score with the best of them.\n   Date: 2025-01-01\n\n7. **NBA News, Rumors, Scores, Standings & Stats - FOX Sports**\n   URL: https://www.foxsports.com/nba\n   2 DAYS AGO\n\n\n\nFOX SPORTS\n\nRockets\' Kevin Durant Latest to Score 31K Career Points During Win vs. Suns\n\n4 DAYS AGO\n\n\n\nFOX SPORTS\n\nLeBron James\' 1,297-Game Double-Digit Scoring Streak Ends vs. Raptors\n\n6 DAYS AGO\n\n\n\nFOX SPORTS\n\nWhat is Futures Betting? How to Read & Bet Futures... LeBron James impresses in Year 23, Chiefs ‘under the most pressure’, Cowboys upset Eagles? | FTF\n\nNOVEMBER 19\n\n\n\nFOX SPORTS\n\nLakers beat Jazz with LeBron and Luka, Are they title contenders with this duo? | The Herd\n\nNOVEMBER 19\n\n\n\nFOX SPORTS\n\nThunder blow out Lakers, Is Los Angeles & Luka not a contender? | The Herd... NOVEMBER 6\n\n\n\nFOX SPORTS\n\nLuka Doncic scores 35 in Lakers win over Spurs, Is Los Angeles a title contender? | The Herd\n\nNOVEMBER 6\n\n\n\nFOX SPORTS\n\nAustin Reaves leads Lakers to win, How far can the big 3 of LeBron, Luka, and Reaves go? | The Herd\n   Date: 2025-12-10\n\n8. **NBA Player News: Latest Reports, Injuries, Transactions**\n   URL: https://www.nbcsports.com/fantasy/basketball/player-news\n   Luka\n\nDončić\n\nLAL\n\nForward-Guard\n\n#77\n\nLuka Dončić had 35 points (11-of-24 FGs, 10-of-15 FTs), five rebounds, eight assists, one steal and three three-pointers against the Spurs on Wednesday.\n\nDončić had another excellent game, his second since missing two games to be present for the birth of his second child. The 26-year-old point guard dropped 35 points against the Spurs after recording his second triple-double of the season against the 76ers on Sunday. He’s been an elite fantasy option in recent weeks.... Recap\n\nLink copied to clipboard!\n\nGrayson\n\nAllen\n\nPHX\n\nGuard\n\n#8\n\nGrayson Allen was ejected after being assessed a flagrant two foul in Wednesday’s loss to the Thunder.\n\nAllen had 10 points in 22 minutes before he was assessed a flagrant foul and ejected against the Thunder on Wednesday. The foul came when Allen shoved Chet Holmgren to the ground mid-play with the Suns trailing by 36 points midway through the third quarter. It’s unclear if the league will further punish Allen.\n   Date: 2025-12-11\n\n9. **More NBA News - ESPN**\n   URL: https://www.espn.com/nba/news/more/_/sport/nba\n   **Thunder match Blazers\' $70M offer to Kanter**\n\nThe Thunder took all three possible days, but decided to match the Portland Trail Blazers \' maximum-level $70 million offer sheet for Enes Kanter.\n\n**LeBron: \'Nightmares\' over Finals loss to GSW**\n\nLeBron James says he has \'nightmares\' over certain situations in the Cleveland Cavaliers\' Finals loss to the Golden State Warriors.... **Nets swoop in to sign Bargnani ahead of Kings**\n\nThe Brooklyn Nets have swooped in to sign former No. 1 overall pick Andrea Bargnani, swiping him away at the 11th hour from the Sacramento Kings.\n\n**Bucks, Henson heading toward deal, sources say**... **Marcus Morris: Suns trade a \'slap in the face\'**\n\nMarcus Morris, who was introduced Friday by the Detroit Pistons, said the way his trade from the Phoenix Suns unfolded was a "slap in the face."\n\n**Saunders: Garnett will be starter next season**\n\nMinnesota Timberwolves president and coach Flip Saunders says he plans to start Kevin Garnett next season and believes he can still make a significant impact at age 39.\n   Date: 2011-12-01\n\n10. **NBA News and Rumors, Advanced NBA Stats, NBA Odds ...**\n   URL: https://www.basketballnews.com\n   10h\n\nMichael Porter Jr. discovers star path with Nets in a career resurgence\n\nyesterday\n\nKevin Love Mentors Jazz Rookie Bailey’s Rapid Rise\n\nyesterday\n\nWhy Cam Whitmore Isn’t Playing for the Wizards\n\nyesterday\n\nJames Harden cracks top-10 all-time scorers, surpassing Carmelo Anthony... After a fruitful showcase in London, Team USA heads on to Paris for the Olympics\n\nBY Mon Anthony Valmoria\n\nJuly 22 2024\n\nCaitlin Clark sets all-time WNBA single-game assist record but Fever fall to Wings\n\nBY Mon Anthony Valmoria\n\nJuly 18 2024\n\nTeam USA decimates Serbia, go up 3-0 in Olympic prep play... June 26 2024\n\nCavaliers to sign Kenny Atkinson to be head coach\n\nBY Mon Anthony Valmoria\n\nJune 24 2024\n\nMalik Monk returns to the Kings on a 4-year, $78 million deal\n\nBY Mon Anthony Valmoria\n\nJune 22 2024... 2024 WNBA Draft Recap: Caitlin Clark goes No.1 to the Indiana Fever\n\nBY Mon Anthony Valmoria\n   Date: 2025-12-10\n\n'}]}, 'id': '3'}
    """


def example_onekey_mcp_gemini_nano_banana_image_generation():
    """
        {"server_id":"perplexity","tool_name":"perplexity_search","tool_input":{"query":"NBA News","max_results":10,"max_tokens_per_page":256,"country":"US"}}
    """
    from mcp_marketplace import OneKeyMCPRouter
    model = "gemini-2.5-flash-image"
    # model = "gemini-3-pro-image-preview"
    example = {"server_name":"gemini-nano-banana",
               "tool_name":"generate_image_nano_banana",
               "tool_input":
                   {"model":f"{model}",
                    "prompt":"MineCraft Steve in Grassland Finding Gold Fighting Zombies",
                    "image_name":"minecraft_steve.png",
                    "output_folder":"/data/python/mcp_tool_use/files-wd/user_5dc1/812fafd1-9d82-4627-8fef-sdf2efsdfdsfsd"
    }}

    ## Todo: Add sandbox
    server_name = example.get("server_name", "")

    ## 1. MCP Initialize POST Request
    ONEKEY_BETA = "BETA_TEST_KEY_OCT_2025"
    router = OneKeyMCPRouter(server_name=server_name, onekey=ONEKEY_BETA)

    ## 2. Check Available Tools, tools/list
    available_tools = router.tools_list(server_name)
    print(f"Server {server_name}|available_tools {available_tools}")

    """
    generate_image_gemini
    Server gemini-nano-banana|available_tools {'result': {'tools': [{'name': 'generate_image_gemini', 'description': ' Generates an image using the Gemini Image API.\n            Supported Models (aliases are internal):\n            The model parameter allows selection between available image generation models.\n            - "gemini-2.5-flash-image" (recommended default for stable, fast response).\n            - "gemini-3-pro-image-preview".\n\n            Aliases for these models are \'nano-banana 2.5\' and \'nano-banana 3 Pro\' respectively.\n            Please use \'gemini-2.5-flash-image\' unless the user specifically requests the Gemini 3 model.\n\n        Args:\n            model: The image generation model to use (see supported models above). Defaults to "gemini-2.5-flash-image".\n            prompt: A detailed text description for the image to be generated.\n            image_name: The filename for the output image, can be a relative path. Defaults to "gemini_output_images.png".\n            output_folder: The optional folder path where the image will be saved (use the user\'s personal directory). If None, uses a server default.\n            aspect_ratio: The aspect ratio of the generated image (e.g., \'16:9\', \'1:1\', \'4:3\'). Defaults to \'16:9\'.\n            image_size: The size/resolution of the generated image (e.g., \'1K\', \'2K\', \'4K\'). Defaults to \'1K\'.\n\n        Return:\n            Dict: Result dictionary containing image path, message, and success status.\n            output_result["image_path"]: str\n            output_result["message"]: str\n            output_result["success"]: bool\n    ', 'inputSchema': {'properties': {'model': {'default': 'gemini-2.5-flash-image', 'title': 'Model', 'type': 'string'}, 'prompt': {'default': 'A detailed, cinematic image of a futuristic city.', 'title': 'Prompt', 'type': 'string'}, 'image_name': {'default': 'gemini_output_images.png', 'title': 'Image Name', 'type': 'string'}, 'output_folder': {'anyOf': [{'type': 'string'}, {'type': 'null'}], 'default': None, 'title': 'Output Folder'}, 'aspect_ratio': {'default': '16:9', 'title': 'Aspect Ratio', 'type': 'string'}, 'image_size': {'default': '1K', 'title': 'Image Size', 'type': 'string'}}, 'title': 'generate_image_geminiArguments', 'type': 'object'}}, {'name': 'generate_image_nano_banana', 'description': ' Get Public Available Stock Symbols from Global Marketplace\n\n        Args:\n            model: The image generation model to use. Defaults to "gemini-2.5-flash-image". Supported Models such as follows Google Gemini Doc, such as "gemini-3-pro-image-preview", "gemini-2.5-flash-image", note that nano-banana is the alias name of the Gemini Image Model. Nano banana 3 Pro refers to Gemini 3 pro preview, and Nono Banana 2.5 refers to Gemini 2.5. Unless specified by user to use Gemini 3 model preview, general \'Neno Banana\' image models, please use \'gemini-2.5-flash-image\' for more stable and fast response.\n            prompt: A detailed text description for the image to be generated.\n            image_name: The filename for the output image, can be a relative path, such as "./new_gemini_image.png", etc. Defaults to "gemini_output_images.png".\n            output_folder: The optional folder path where the image will be saved. Please use the users\' personal directory for this path. If None, uses a default location to the root folder of the server/image\n            aspect_ratio: The aspect ratio of the generated image (e.g., \'16:9\', \'1:1\', \'4:3\'), defaults to \'16:9\'.\n            image_size: The size/resolution of the generated image (e.g., \'1K\', \'2K\', \'4K\'), defaults to \'1K\'.\n\n        Return:\n            Dict:  output_result is the result dict of MCP returned\n            output_result["image_path"] = full_path: str\n            output_result["message"] = output_message: str\n            output_result["success"] = success: bool\n    ', 'inputSchema': {'properties': {'model': {'default': 'gemini-2.5-flash-image', 'title': 'Model', 'type': 'string'}, 'prompt': {'default': 'A detailed, cinematic image of a futuristic city.', 'title': 'Prompt', 'type': 'string'}, 'image_name': {'default': 'gemini_output_images.png', 'title': 'Image Name', 'type': 'string'}, 'output_folder': {'anyOf': [{'type': 'string'}, {'type': 'null'}], 'default': None, 'title': 'Output Folder'}, 'aspect_ratio': {'default': '16:9', 'title': 'Aspect Ratio', 'type': 'string'}, 'image_size': {'default': '1K', 'title': 'Image Size', 'type': 'string'}}, 'title': 'generate_image_nano_bananaArguments', 'type': 'object'}}]}, 'jsonrpc': '2.0', 'id': '2'}    
    """

    ## Your LLM Code
    ## 3. Run Tool, Post tools/call request
    result_json = router.tools_call(server_name, example.get("tool_name", ""),
                                    example.get("tool_input", {}))
    print(
        f"Server {server_name}|tool_name {example.get("tool_name", "")} | tool_input {example.get("tool_input", {})} |result_json {result_json}")

    """
        Server gemini-nano-banana|tool_name generate_image_nano_banana | tool_input {'model': 'gemini-2.5-flash-image', 'prompt': 'MineCraft Steve in Grassland Finding Gold Fighting Zombies', 'image_name': 'minecraft_steve.png', 'output_folder': '/data/python/mcp_tool_use/files-wd/user_5dc1/812fafd1-9d82-4627-8fef-sdf2efsdfdsfsd'} |result_json {'jsonrpc': '2.0', 'result': {'success': True, 'content': [{'type': 'text', 'text': ''}]}, 'id': '3'}
    """

    ### 图像


def example_onekey_mcp_tavily_search_map():
    """
        Example of Using DeepNLP OneKey MCP Router to Access Commercial MCPs
    """
    from mcp_marketplace import OneKeyMCPRouter

    example = {"server_id":"tavily-remote-mcp",
               "tool_name":"tavily_search",
               "tool_input":{"query":"NFL game news","topic":"news","time_range":"day"}}
    server_name = example.get("server_name", "")

    ## 1. MCP Initialize POST Request
    ONEKEY_BETA = "BETA_TEST_KEY_OCT_2025"
    router = OneKeyMCPRouter(server_name=server_name, onekey=ONEKEY_BETA)

    ## 2. Check Available Tools, tools/list
    available_tools = router.tools_list(server_name)
    print(f"Server {server_name}|available_tools {available_tools}")

    ## Your LLM Code

    ## 3. Run Tool, Post tools/call request
    result_json = router.tools_call(server_name, example.get("tool_name", ""), example.get("tool_input", {}))
    print(
        f"Server {server_name}|tool_name {example.get("tool_name", "")} | tool_input {example.get("tool_input", {})} |result_json {result_json}")


def example_onekey_mcp_firecrawl_search_map():
    """
        Example of Using DeepNLP OneKey MCP Router to Access Commercial MCPs
    """
    from mcp_marketplace import OneKeyMCPRouter

    example = {"server_id":"firecrawl-mcp","tool_name":"firecrawl_search","tool_input":{"query": "NFL Games", "limit": "30", "tbs": "", "filter": "", "location": "", "sources": "", "scrapeOptions": ""}}
    server_name = example.get("server_name", "")

    ## 1. MCP Initialize POST Request
    ONEKEY_BETA = "BETA_TEST_KEY_OCT_2025"
    router = OneKeyMCPRouter(server_name=server_name, onekey=ONEKEY_BETA)

    ## 2. Check Available Tools, tools/list
    available_tools = router.tools_list(server_name)
    print(f"Server {server_name}|available_tools {available_tools}")

    ## Your LLM Code

    ## 3. Run Tool, Post tools/call request
    result_json = router.tools_call(server_name, example.get("tool_name", ""), example.get("tool_input", {}))
    print(
        f"Server {server_name}|tool_name {example.get("tool_name", "")} | tool_input {example.get("tool_input", {})} |result_json {result_json}")

def example_onekey_brave_search_map():
    """
        Example of Using DeepNLP OneKey MCP Router to Access Commercial MCPs
    """
    from mcp_marketplace import OneKeyMCPRouter

    example = {"server_id": "brave-search", "tool_name": "brave_web_search",
         "tool_input": {"query": "NFL Games", "count": 10, "offset": 0}}
    server_name = example.get("server_name", "")

    ## 1. MCP Initialize POST Request
    ONEKEY_BETA = "BETA_TEST_KEY_OCT_2025"
    router = OneKeyMCPRouter(server_name=server_name, onekey=ONEKEY_BETA)

    ## 2. Check Available Tools, tools/list
    available_tools = router.tools_list(server_name)
    print(f"Server {server_name}|available_tools {available_tools}")

    ## Your LLM Code

    ## 3. Run Tool, Post tools/call request
    result_json = router.tools_call(server_name, example.get("tool_name", ""), example.get("tool_input", {}))
    print(
        f"Server {server_name}|tool_name {example.get("tool_name", "")} | tool_input {example.get("tool_input", {})} |result_json {result_json}")


def example_onekey_bing_image_search_map():
    """
        Example of Using DeepNLP OneKey MCP Router to Access Commercial MCPs
    """
    from mcp_marketplace import OneKeyMCPRouter

    example = {"server_id":"bing-image-search-mcp","tool_name":"search_images","tool_input":{"query": "Minecraft Grassland", "limit": "30"}}
    server_name = example.get("server_name", "")

    ## 1. MCP Initialize POST Request
    ONEKEY_BETA = "BETA_TEST_KEY_OCT_2025"
    router = OneKeyMCPRouter(server_name=server_name, onekey=ONEKEY_BETA)

    ## 2. Check Available Tools, tools/list
    available_tools = router.tools_list(server_name)
    print(f"Server {server_name}|available_tools {available_tools}")

    ## Your LLM Code

    ## 3. Run Tool, Post tools/call request
    result_json = router.tools_call(server_name, example.get("tool_name", ""), example.get("tool_input", {}))
    print(
        f"Server {server_name}|tool_name {example.get("tool_name", "")} | tool_input {example.get("tool_input", {})} |result_json {result_json}")


def example_onekey_figma_map():
    """
        Example of Using DeepNLP OneKey MCP Router to Access Commercial MCPs
    """
    from mcp_marketplace import OneKeyMCPRouter

    example = {"server_id":"Framelink Figma MCP","tool_name":"get_figma_data","tool_input":{"fileKey":"ppWn2zGh1EdJ6MzuxknSVa","nodeId":"0-1","depth":1}}
    server_name = example.get("server_name", "")

    ## 1. MCP Initialize POST Request
    ONEKEY_BETA = "BETA_TEST_KEY_OCT_2025"
    router = OneKeyMCPRouter(server_name=server_name, onekey=ONEKEY_BETA)

    ## 2. Check Available Tools, tools/list
    available_tools = router.tools_list(server_name)
    print(f"Server {server_name}|available_tools {available_tools}")

    ## Your LLM Code

    ## 3. Run Tool, Post tools/call request
    result_json = router.tools_call(server_name, example.get("tool_name", ""), example.get("tool_input", {}))
    print(
        f"Server {server_name}|tool_name {example.get("tool_name", "")} | tool_input {example.get("tool_input", {})} |result_json {result_json}")


def example_onekey_notion_api_map():
    """
        Example of Using DeepNLP OneKey MCP Router to Access Commercial MCPs
    """
    from mcp_marketplace import OneKeyMCPRouter

    example = {"server_id":"notionApi","tool_name":"API-get-user","tool_input":{"user_id":"Derek"}}
    server_name = example.get("server_name", "")

    ## 1. MCP Initialize POST Request
    ONEKEY_BETA = "BETA_TEST_KEY_OCT_2025"
    router = OneKeyMCPRouter(server_name=server_name, onekey=ONEKEY_BETA)

    ## 2. Check Available Tools, tools/list
    available_tools = router.tools_list(server_name)
    print(f"Server {server_name}|available_tools {available_tools}")

    ## Your LLM Code

    ## 3. Run Tool, Post tools/call request
    result_json = router.tools_call(server_name, example.get("tool_name", ""), example.get("tool_input", {}))
    print(
        f"Server {server_name}|tool_name {example.get("tool_name", "")} | tool_input {example.get("tool_input", {})} |result_json {result_json}")


def example_onekey_github_map():
    """
        Example of Using DeepNLP OneKey MCP Router to Access Commercial MCPs
    """
    from mcp_marketplace import OneKeyMCPRouter

    example = {"server_id":"github","tool_name":"search_code","tool_input":{"order":"","page":1,"perPage":10,"query":"AI AGENT","sort":""}}
    server_name = example.get("server_name", "")

    ## 1. MCP Initialize POST Request
    ONEKEY_BETA = "BETA_TEST_KEY_OCT_2025"
    router = OneKeyMCPRouter(server_name=server_name, onekey=ONEKEY_BETA)

    ## 2. Check Available Tools, tools/list
    available_tools = router.tools_list(server_name)
    print(f"Server {server_name}|available_tools {available_tools}")

    ## Your LLM Code

    ## 3. Run Tool, Post tools/call request
    result_json = router.tools_call(server_name, example.get("tool_name", ""), example.get("tool_input", {}))
    print(
        f"Server {server_name}|tool_name {example.get("tool_name", "")} | tool_input {example.get("tool_input", {})} |result_json {result_json}")

def example_onekey_mcp_server_chat_map():
    """
        Example of Using DeepNLP OneKey MCP Router to Access Commercial MCPs
    """
    from mcp_marketplace import OneKeyMCPRouter

    example = {"server_id":"mcp-server-chart","tool_name":"generate_bar_chart","tool_input":{"data":[{"category":"Graduated within 3 years","value":25},{"category":"Graduated more than 3 years ago","value":75}],"title":"Employee Graduation Timeline"}}
    server_name = example.get("server_name", "")

    ## 1. MCP Initialize POST Request
    ONEKEY_BETA = "BETA_TEST_KEY_OCT_2025"
    router = OneKeyMCPRouter(server_name=server_name, onekey=ONEKEY_BETA)

    ## 2. Check Available Tools, tools/list
    available_tools = router.tools_list(server_name)
    print(f"Server {server_name}|available_tools {available_tools}")

    ## Your LLM Code

    ## 3. Run Tool, Post tools/call request
    result_json = router.tools_call(server_name, example.get("tool_name", ""), example.get("tool_input", {}))
    print(
        f"Server {server_name}|tool_name {example.get("tool_name", "")} | tool_input {example.get("tool_input", {})} |result_json {result_json}")

def example_onekey_excel_map():
    """
        Example of Using DeepNLP OneKey MCP Router to Access Commercial MCPs
    """
    from mcp_marketplace import OneKeyMCPRouter

    example = \
        {"server_id":"mcp-server-chart","tool_name":"generate_bar_chart","tool_input":{"data":[{"category":"Graduated within 3 years","value":25},{"category":"Graduated more than 3 years ago","value":75}],"title":"Employee Graduation Timeline"}}
    server_name = example.get("server_name", "")

    ## 1. MCP Initialize POST Request
    ONEKEY_BETA = "BETA_TEST_KEY_OCT_2025"
    router = OneKeyMCPRouter(server_name=server_name, onekey=ONEKEY_BETA)

    ## 2. Check Available Tools, tools/list
    available_tools = router.tools_list(server_name)
    print(f"Server {server_name}|available_tools {available_tools}")

    ## Your LLM Code

    ## 3. Run Tool, Post tools/call request
    result_json = router.tools_call(server_name, example.get("tool_name", ""), example.get("tool_input", {}))
    print(
        f"Server {server_name}|tool_name {example.get("tool_name", "")} | tool_input {example.get("tool_input", {})} |result_json {result_json}")

def example_onekey_finance_stock_map():
    """
        Example of Using DeepNLP OneKey MCP Router to Access Commercial MCPs
    """
    from mcp_marketplace import OneKeyMCPRouter

    example = \
        {"server_id":"finance-agent-mcp-server","tool_name":"get_stock_price_global_market","tool_input":{"symbol_list":["700","1024"],"market":"HK"}}
    server_name = example.get("server_name", "")

    ## 1. MCP Initialize POST Request
    ONEKEY_BETA = "BETA_TEST_KEY_OCT_2025"
    router = OneKeyMCPRouter(server_name=server_name, onekey=ONEKEY_BETA)

    ## 2. Check Available Tools, tools/list
    available_tools = router.tools_list(server_name)
    print(f"Server {server_name}|available_tools {available_tools}")

    ## Your LLM Code

    ## 3. Run Tool, Post tools/call request
    result_json = router.tools_call(server_name, example.get("tool_name", ""), example.get("tool_input", {}))
    print(
        f"Server {server_name}|tool_name {example.get("tool_name", "")} | tool_input {example.get("tool_input", {})} |result_json {result_json}")

def example_onekey_alipay_map():
    """
        Example of Using DeepNLP OneKey MCP Router to Access Commercial MCPs
    """
    from mcp_marketplace import OneKeyMCPRouter

    example = \
        {"server_id":"mcp-server-alipay","tool_name":"create-mobile-alipay-payment","tool_input":{"outTradeNo":"123","totalAmount":"30","orderTitle":"Order Pending Payment O1"}}
    server_name = example.get("server_name", "")

    ## 1. MCP Initialize POST Request
    ONEKEY_BETA = "BETA_TEST_KEY_OCT_2025"
    router = OneKeyMCPRouter(server_name=server_name, onekey=ONEKEY_BETA)

    ## 2. Check Available Tools, tools/list
    available_tools = router.tools_list(server_name)
    print(f"Server {server_name}|available_tools {available_tools}")

    ## Your LLM Code

    ## 3. Run Tool, Post tools/call request
    result_json = router.tools_call(server_name, example.get("tool_name", ""), example.get("tool_input", {}))
    print(
        f"Server {server_name}|tool_name {example.get("tool_name", "")} | tool_input {example.get("tool_input", {})} |result_json {result_json}")


def example_onekey_paypal_map():
    """
        Example of Using DeepNLP OneKey MCP Router to Access Commercial MCPs
    """
    from mcp_marketplace import OneKeyMCPRouter

    example = \
        {"server_id":"paypal","tool_name":"create_order","tool_input":{"currencyCode":"USD","items":"Good 1","discount":"0.5","shippingCost":"10.0","shippingAddress":"1111 Mary Ln,San Jose,99999","notes":"","returnUrl":"","cancelUrl":""}}
    server_name = example.get("server_name", "")

    ## 1. MCP Initialize POST Request
    ONEKEY_BETA = "BETA_TEST_KEY_OCT_2025"
    router = OneKeyMCPRouter(server_name=server_name, onekey=ONEKEY_BETA)

    ## 2. Check Available Tools, tools/list
    available_tools = router.tools_list(server_name)
    print(f"Server {server_name}|available_tools {available_tools}")

    ## Your LLM Code

    ## 3. Run Tool, Post tools/call request
    result_json = router.tools_call(server_name, example.get("tool_name", ""), example.get("tool_input", {}))
    print(
        f"Server {server_name}|tool_name {example.get("tool_name", "")} | tool_input {example.get("tool_input", {})} |result_json {result_json}")
