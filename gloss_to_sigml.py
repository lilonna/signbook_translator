def gloss_to_sigml(gloss_list):
    template = '''<sigml>
    <hns_sign gloss="{gloss}" />
</sigml>'''
    return [template.format(gloss=word) for word in gloss_list]

# Example usage
if __name__ == "__main__":
    example_gloss = ["BOY", "EAT", "APPLE"]
    sigml_list = gloss_to_sigml(example_gloss)
    for i, sigml in enumerate(sigml_list, 1):
        print(f"Sign {i}:\n{sigml}\n")