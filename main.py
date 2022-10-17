from urllib.parse import urlparse, urlunparse


# cleanup data
def fix_url(url_in):
    """fix broken url for certain vocabularies"""
    url_in_ = urlparse(url_in)
    if url_in_.netloc == "vocabularies.cessda.eu":
        # TODO replace code with voc from the API res
        new_path = str(url_in_.path.split("/")[2].replace("[CODE]", "sam"))
        new_url = url_in_._replace(netloc="rdf-vocabulary.ddialliance.org")._replace(
            path=new_path
        )
    return urlunparse(new_url)

def main():
    """main entry point"""
    # asyncio.run(get_data())
    # print(json.dumps(result))
    print(
        fix_url(
            "https://vocabularies.cessda.eu/vocabulary/CessdaPersistentIdentifierTypes_[CODE]?v=1.0"
        )
    )


if __name__ == "__main__":
    main()
