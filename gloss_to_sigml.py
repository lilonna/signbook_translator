# #gloss_to_sigml.py
# def gloss_to_sigml(gloss_list):
#     template = '''<sigml>
#     <hns_sign gloss="{gloss}" />
# </sigml>'''
#     return [template.format(gloss=word) for word in gloss_list]
def gloss_to_sigml(glosses):
    signs = "\n".join([f'<hns_sign gloss="{word}" />' for word in glosses])
    return f'<?xml version="1.0" encoding="utf-8"?>\n<sigml>\n{signs}\n</sigml>'



# Example usage
if __name__ == "__main__":
    example_gloss = ["BOY", "EAT", "APPLE"]
    sigml_list = gloss_to_sigml(example_gloss)
    for i, sigml in enumerate(sigml_list, 1):
        print(f"Sign {i}:\n{sigml}\n")