import conect
import json


def edit_title(arr):
    sprit_num = 10
    arr_2 = []
    arr_2 = list(map(lambda x:f"{x[0]+1}.{x[1]}",enumerate(arr)))
    print(arr_2)
    reslte = []
    
    for i in range(0,len(arr_2),sprit_num):
        reslte.append(arr_2[i:i+sprit_num])
    
    return reslte

def send(prompt):
    conect.init()
    conect.send_message(prompt)
    return conect.response.choices[0].message.content

def list_search(arr, keyword_list):
    result = []
    for item in arr:
        found = False
        for keyword in keyword_list:
            if keyword in item:
                found = True
                break
        result.append(found)
    
    return result

def res_check(input_text, response):
    try:
        res_json = json.loads(response)
        if not len(input_text) == len(res_json):
            print("Error: The number of input titles does not match the number of output titles.")
            print(f"Input length: {len(input_text)}, Output length: {len(res_json)}")
            return False
        else:
            for i in list_search(input_text, list(res_json)):
                if not i:
                    print("Error: One or more input titles were not found in the output.",i)
                    return False
                else:
                    return True
    except json.JSONDecodeError:
        print("JSON Decode Error: Invalid JSON format.")
        return False

def main(text):
    prompt = edit_title(text)
    res = send(prompt)
    result = res_check(text, res)


if __name__ == "__main__":
    test_1 = "1.MIMI - サイエンス (feat.重音テトSV),2.『ソルティメロウ』 / feat. 可不,3.『天使の涙』 / feat.初音ミク,4.『アンコールダンス』/ feat. 重音テトSV,5.『夜と幸せ』/ feat. 詩の出素。,6.『桜の戦略 』/ MIMI feat. マス,7.『お砂糖哀歌』 / feat. 初音ミク,8.『恋しくなったら手を叩こう』/ MIMI feat.花鏡紅璃,9.『恋しくなったら手を叩こう』 / feat.重音テトSV,10.ヒューマとニズム-Hata"
    test_list = test_1.split(",")
    test_list_2 = ["MIMI - サイエンス (feat.重音テトSV)",
                    "ソルティメロウ』 / feat. 可不",
                    "『天使の涙』 / feat.初音ミク",
                    "『アンコールダンス』/ feat. 重音テトSV",
                    "『夜と幸せ』/ feat. 詩の出素。",
                    "『桜の戦略 』/ MIMI feat. マス",
                    "『お砂糖哀歌』 / feat. 初音ミク",
                    "『恋しくなったら手を叩こう』/ MIMI feat.花鏡紅璃",
                    "『恋しくなったら手を叩こう』 / feat.重音テトSV",
                    "ヒューマとニズム-Hata",
                    "暴飲暴食P 「うそつきマカロン」feat. 重音テト ",
                    "あんずの花/ すりぃ feat.ねね(Official Music Video)",
                    "ヨルシカ「ただ君に晴れ」Music Video",
                    "[self cover] The Beast. /スペクタルP feat 可不"]

    res = edit_title(test_list_2)
    print(res)
    # result = send(test_1)
    # result_json = json.loads(result)
    # print(result_json)