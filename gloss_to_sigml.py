
def gloss_to_sigml(glosses):
    signs = "\n".join([f'<hns_sign gloss="{word}" />' for word in glosses])
    return f'<?xml version="1.0" encoding="utf-8"?>\n<sigml>\n{signs}\n</sigml>'



