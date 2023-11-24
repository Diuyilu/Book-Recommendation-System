from flask import jsonify

def history_serializer(historyinfo):
    history_list = []
    for info in historyinfo:
        history_dict = {
            'xh': info.xh,
            'xb': info.xb,
            'nl': info.nl,
            'syd': info.syd,
            'pycc': info.pycc,
            'sznj': info.sznj,
            'xy': info.xy,
            'tsbh': info.tsbh,
            'tsmc': info.tsmc,
            'czrq': info.czrq,
            'jyzt': info.jyzt
        }
        history_list.append(history_dict)
    return jsonify({'history_list': history_list, "status": 1})