# invenio-subjects-cessda

 CESSDA Vocabulary for [InvenioRDM](https://inveniosoftware.org/products/rdm/)
This package is inspired by [invenio-subjects-mesh](https://github.com/galterlibrary/invenio-subjects-mesh)
Install this extension to get CESSDA Voc. subject terms used to index and retrieve materials in the STI Repository into your instance.

## Installation

From your instance active venv:
```console
pip install invenio-subjects-cessda
```

This will add it to your Pipfile.

you can double check by running
```console
pip freeze | grep invenio-subjects-cessda
```
in your invenio instance run:
```console
invenio rdm-records fixtures
invenio-cli run
```
the above commands could take long time to finish so be patient.

### Versions

This repository follows [SemVer versioning](https://semver.org/):


## Usage

There are 2 types of users for this package. Maintainers of the package and instance administrators.

### Instance administrators

For instance administrators, after you have installed the extension as per the steps above,
please read [Invenio subjects documentation](https://inveniordm.docs.cern.ch/customize/vocabularies/subjects/)

**Note**

There is always a room for improvements specially the performance, feel free to drop a PR for that.
TODO:
- write more tests
- improve performance, maybe using Pandas or numpy instead, etc ...


## Maintainers
TODO
- how to fetch new versions
- setup dev env
- run tests

> When doing tests you will get a warning from [black formatter](https://github.com/shopkeep/pytest-black/issues/55), should bump pytest-black version when it's done

```console
pip install -e ".[tests]"
```
```console
./run-tests
```


## Example:
```json
{"id": "https://id.nlm.nih.gov/mesh/D000071696Q000379", "scheme": "MeSH", "subject": "Proteogenomics/methods"}
{"id": "https://id.nlm.nih.gov/mesh/D000071696Q000458", "scheme": "MeSH", "subject": "Proteogenomics/organization & administration"}
{"id": "https://id.nlm.nih.gov/mesh/D000071696Q000706", "scheme": "MeSH", "subject": "Proteogenomics/statistics & numerical data"}
{"id": "https://id.nlm.nih.gov/mesh/D000071696Q000592", "scheme": "MeSH", "subject": "Proteogenomics/standards"}
{"id": "https://id.nlm.nih.gov/mesh/D000071696Q000639", "scheme": "MeSH", "subject": "Proteogenomics/trends"}
{"id": "https://id.nlm.nih.gov/mesh/D000071697", "scheme": "MeSH", "subject": "Cellulite"}
{"id": "https://id.nlm.nih.gov/mesh/D000071697Q000097", "scheme": "MeSH", "subject": "Cellulite/blood"}
{"id": "https://id.nlm.nih.gov/mesh/D000071697Q000134", "scheme": "MeSH", "subject": "Cellulite/cerebrospinal fluid"}
{"id": "https://id.nlm.nih.gov/mesh/D000071697Q000139", "scheme": "MeSH", "subject": "Cellulite/chemically induced"}
{"id": "https://id.nlm.nih.gov/mesh/D000071697Q000145", "scheme": "MeSH", "subject": "Cellulite/classification"}
{"id": "https://id.nlm.nih.gov/mesh/D000071697Q000151", "scheme": "MeSH", "subject": "Cellulite/congenital"}
{"id": "https://id.nlm.nih.gov/mesh/D000071697Q000150", "scheme": "MeSH", "subject": "Cellulite/complications"}
{"id": "https://id.nlm.nih.gov/mesh/D000071697Q000000981", "scheme": "MeSH", "subject": "Cellulite/diagnostic imaging"}
{"id": "https://id.nlm.nih.gov/mesh/D000071697Q000178", "scheme": "MeSH", "subject": "Cellulite/diet therapy"}
{"id": "https://id.nlm.nih.gov/mesh/D000071697Q000175", "scheme": "MeSH", "subject": "Cellulite/diagnosis"}
{"id": "https://id.nlm.nih.gov/mesh/D000071697Q000188", "scheme": "MeSH", "subject": "Cellulite/drug therapy"}
{"id": "https://id.nlm.nih.gov/mesh/D000071697Q000191", "scheme": "MeSH", "subject": "Cellulite/economics"}
{"id": "https://id.nlm.nih.gov/mesh/D000071697Q000208", "scheme": "MeSH", "subject": "Cellulite/ethnology"}
{"id": "https://id.nlm.nih.gov/mesh/D000071697Q000196", "scheme": "MeSH", "subject": "Cellulite/embryology"}
{"id": "https://id.nlm.nih.gov/mesh/D000071697Q000201", "scheme": "MeSH", "subject": "Cellulite/enzymology"}
{"id": "https://id.nlm.nih.gov/mesh/D000071697Q000453", "scheme": "MeSH", "subject": "Cellulite/epidemiology"}
{"id": "https://id.nlm.nih.gov/mesh/D000071697Q000209", "scheme": "MeSH", "subject": "Cellulite/etiology"}
{"id": "https://id.nlm.nih.gov/mesh/D000071697Q000235", "scheme": "MeSH", "subject": "Cellulite/genetics"}
{"id": "https://id.nlm.nih.gov/mesh/D000071697Q000266", "scheme": "MeSH", "subject": "Cellulite/history"}
{"id": "https://id.nlm.nih.gov/mesh/D000071697Q000276", "scheme": "MeSH", "subject": "Cellulite/immunology"}
{"id": "https://id.nlm.nih.gov/mesh/D000071697Q000378", "scheme": "MeSH", "subject": "Cellulite/metabolism"}
{"id": "https://id.nlm.nih.gov/mesh/D000071697Q000382", "scheme": "MeSH", "subject": "Cellulite/microbiology"}
{"id": "https://id.nlm.nih.gov/mesh/D000071697Q000401", "scheme": "MeSH", "subject": "Cellulite/mortality"}
{"id": "https://id.nlm.nih.gov/mesh/D000071697Q000451", "scheme": "MeSH", "subject": "Cellulite/nursing"}
{"id": "https://id.nlm.nih.gov/mesh/D000071697Q000473", "scheme": "MeSH", "subject": "Cellulite/pathology"}
{"id": "https://id.nlm.nih.gov/mesh/D000071697Q000517", "scheme": "MeSH", "subject": "Cellulite/prevention & control"}
{"id": "https://id.nlm.nih.gov/mesh/D000071697Q000503", "scheme": "MeSH", "subject": "Cellulite/physiopathology"}
{"id": "https://id.nlm.nih.gov/mesh/D000071697Q000469", "scheme": "MeSH", "subject": "Cellulite/parasitology"}
{"id": "https://id.nlm.nih.gov/mesh/D000071697Q000523", "scheme": "MeSH", "subject": "Cellulite/psychology"}
{"id": "https://id.nlm.nih.gov/mesh/D000071697Q000534", "scheme": "MeSH", "subject": "Cellulite/rehabilitation"}
{"id": "https://id.nlm.nih.gov/mesh/D000071697Q000532", "scheme": "MeSH", "subject": "Cellulite/radiotherapy"}
{"id": "https://id.nlm.nih.gov/mesh/D000071697Q000601", "scheme": "MeSH", "subject": "Cellulite/surgery"}
{"id": "https://id.nlm.nih.gov/mesh/D000071697Q000628", "scheme": "MeSH", "subject": "Cellulite/therapy"}
{"id": "https://id.nlm.nih.gov/mesh/D000071697Q000652", "scheme": "MeSH", "subject": "Cellulite/urine"}
{"id": "https://id.nlm.nih.gov/mesh/D000071697Q000662", "scheme": "MeSH", "subject": "Cellulite/veterinary"}
{"id": "https://id.nlm.nih.gov/mesh/D000071697Q000821", "scheme": "MeSH", "subject": "Cellulite/virology"}
{"id": "https://id.nlm.nih.gov/mesh/D000071698", "scheme": "MeSH", "subject": "Latent Autoimmune Diabetes in Adults"}
{"id": "https://id.nlm.nih.gov/mesh/D000071698Q000097", "scheme": "MeSH", "subject": "Latent Autoimmune Diabetes in Adults/blood"}
{"id": "https://id.nlm.nih.gov/mesh/D000071698Q000134", "scheme": "MeSH", "subject": "Latent Autoimmune Diabetes in Adults/cerebrospinal fluid"}
{"id": "https://id.nlm.nih.gov/mesh/D000071698Q000139", "scheme": "MeSH", "subject": "Latent Autoimmune Diabetes in Adults/chemically induced"}
{"id": "https://id.nlm.nih.gov/mesh/D000071698Q000145", "scheme": "MeSH", "subject": "Latent Autoimmune Diabetes in Adults/classification"}
{"id": "https://id.nlm.nih.gov/mesh/D000071698Q000151", "scheme": "MeSH", "subject": "Latent Autoimmune Diabetes in Adults/congenital"}
{"id": "https://id.nlm.nih.gov/mesh/D000071698Q000150", "scheme": "MeSH", "subject": "Latent Autoimmune Diabetes in Adults/complications"}
{"id": "https://id.nlm.nih.gov/mesh/D000071698Q000000981", "scheme": "MeSH", "subject": "Latent Autoimmune Diabetes in Adults/diagnostic imaging"}
{"id": "https://id.nlm.nih.gov/mesh/D000071698Q000178", "scheme": "MeSH", "subject": "Latent Autoimmune Diabetes in Adults/diet therapy"}
{"id": "https://id.nlm.nih.gov/mesh/D000071698Q000175", "scheme": "MeSH", "subject": "Latent Autoimmune Diabetes in Adults/diagnosis"}
{"id": "https://id.nlm.nih.gov/mesh/D000071698Q000188", "scheme": "MeSH", "subject": "Latent Autoimmune Diabetes in Adults/drug therapy"}
{"id": "https://id.nlm.nih.gov/mesh/D000071698Q000191", "scheme": "MeSH", "subject": "Latent Autoimmune Diabetes in Adults/economics"}
{"id": "https://id.nlm.nih.gov/mesh/D000071698Q000208", "scheme": "MeSH", "subject": "Latent Autoimmune Diabetes in Adults/ethnology"}
{"id": "https://id.nlm.nih.gov/mesh/D000071698Q000196", "scheme": "MeSH", "subject": "Latent Autoimmune Diabetes in Adults/embryology"}
{"id": "https://id.nlm.nih.gov/mesh/D000071698Q000201", "scheme": "MeSH", "subject": "Latent Autoimmune Diabetes in Adults/enzymology"}
{"id": "https://id.nlm.nih.gov/mesh/D000071698Q000453", "scheme": "MeSH", "subject": "Latent Autoimmune Diabetes in Adults/epidemiology"}
{"id": "https://id.nlm.nih.gov/mesh/D000071698Q000209", "scheme": "MeSH", "subject": "Latent Autoimmune Diabetes in Adults/etiology"}
{"id": "https://id.nlm.nih.gov/mesh/D000071698Q000235", "scheme": "MeSH", "subject": "Latent Autoimmune Diabetes in Adults/genetics"}
{"id": "https://id.nlm.nih.gov/mesh/D000071698Q000266", "scheme": "MeSH", "subject": "Latent Autoimmune Diabetes in Adults/history"}
{"id": "https://id.nlm.nih.gov/mesh/D000071698Q000276", "scheme": "MeSH", "subject": "Latent Autoimmune Diabetes in Adults/immunology"}
{"id": "https://id.nlm.nih.gov/mesh/D000071698Q000378", "scheme": "MeSH", "subject": "Latent Autoimmune Diabetes in Adults/metabolism"}
{"id": "https://id.nlm.nih.gov/mesh/D000071698Q000382", "scheme": "MeSH", "subject": "Latent Autoimmune Diabetes in Adults/microbiology"}
{"id": "https://id.nlm.nih.gov/mesh/D000071698Q000401", "scheme": "MeSH", "subject": "Latent Autoimmune Diabetes in Adults/mortality"}
{"id": "https://id.nlm.nih.gov/mesh/D000071698Q000451", "scheme": "MeSH", "subject": "Latent Autoimmune Diabetes in Adults/nursing"}
{"id": "https://id.nlm.nih.gov/mesh/D000071698Q000473", "scheme": "MeSH", "subject": "Latent Autoimmune Diabetes in Adults/pathology"}
{"id": "https://id.nlm.nih.gov/mesh/D000071698Q000517", "scheme": "MeSH", "subject": "Latent Autoimmune Diabetes in Adults/prevention & control"}
{"id": "https://id.nlm.nih.gov/mesh/D000071698Q000503", "scheme": "MeSH", "subject": "Latent Autoimmune Diabetes in Adults/physiopathology"}
{"id": "https://id.nlm.nih.gov/mesh/D000071698Q000469", "scheme": "MeSH", "subject": "Latent Autoimmune Diabetes in Adults/parasitology"}
{"id": "https://id.nlm.nih.gov/mesh/D000071698Q000523", "scheme": "MeSH", "subject": "Latent Autoimmune Diabetes in Adults/psychology"}
{"id": "https://id.nlm.nih.gov/mesh/D000071698Q000534", "scheme": "MeSH", "subject": "Latent Autoimmune Diabetes in Adults/rehabilitation"}
{"id": "https://id.nlm.nih.gov/mesh/D000071698Q000532", "scheme": "MeSH", "subject": "Latent Autoimmune Diabetes in Adults/radiotherapy"}
{"id": "https://id.nlm.nih.gov/mesh/D000071698Q000601", "scheme": "MeSH", "subject": "Latent Autoimmune Diabetes in Adults/surgery"}
{"id": "https://id.nlm.nih.gov/mesh/D000071698Q000628", "scheme": "MeSH", "subject": "Latent Autoimmune Diabetes in Adults/therapy"}
{"id": "https://id.nlm.nih.gov/mesh/D000071698Q000652", "scheme": "MeSH", "subject": "Latent Autoimmune Diabetes in Adults/urine"}
{"id": "https://id.nlm.nih.gov/mesh/D000071698Q000662", "scheme": "MeSH", "subject": "Latent Autoimmune Diabetes in Adults/veterinary"}
{"id": "https://id.nlm.nih.gov/mesh/D000071698Q000821", "scheme": "MeSH", "subject": "Latent Autoimmune Diabetes in Adults/virology"}
{"id": "https://id.nlm.nih.gov/mesh/D000071699", "scheme": "MeSH", "subject": "Bilateral Vestibulopathy"}
{"id": "https://id.nlm.nih.gov/mesh/D000071699Q000097", "scheme": "MeSH", "subject": "Bilateral Vestibulopathy/blood"}
{"id": "https://id.nlm.nih.gov/mesh/D000071699Q000134", "scheme": "MeSH", "subject": "Bilateral Vestibulopathy/cerebrospinal fluid"}
{"id": "https://id.nlm.nih.gov/mesh/D000071699Q000139", "scheme": "MeSH", "subject": "Bilateral Vestibulopathy/chemically induced"}
{"id": "https://id.nlm.nih.gov/mesh/D000071699Q000145", "scheme": "MeSH", "subject": "Bilateral Vestibulopathy/classification"}
{"id": "https://id.nlm.nih.gov/mesh/D000071699Q000151", "scheme": "MeSH", "subject": "Bilateral Vestibulopathy/congenital"}
{"id": "https://id.nlm.nih.gov/mesh/D000071699Q000150", "scheme": "MeSH", "subject": "Bilateral Vestibulopathy/complications"}
{"id": "https://id.nlm.nih.gov/mesh/D000071699Q000000981", "scheme": "MeSH", "subject": "Bilateral Vestibulopathy/diagnostic imaging"}
{"id": "https://id.nlm.nih.gov/mesh/D000071699Q000178", "scheme": "MeSH", "subject": "Bilateral Vestibulopathy/diet therapy"}
{"id": "https://id.nlm.nih.gov/mesh/D000071699Q000175", "scheme": "MeSH", "subject": "Bilateral Vestibulopathy/diagnosis"}
{"id": "https://id.nlm.nih.gov/mesh/D000071699Q000188", "scheme": "MeSH", "subject": "Bilateral Vestibulopathy/drug therapy"}
{"id": "https://id.nlm.nih.gov/mesh/D000071699Q000191", "scheme": "MeSH", "subject": "Bilateral Vestibulopathy/economics"}
{"id": "https://id.nlm.nih.gov/mesh/D000071699Q000208", "scheme": "MeSH", "subject": "Bilateral Vestibulopathy/ethnology"}
{"id": "https://id.nlm.nih.gov/mesh/D000071699Q000196", "scheme": "MeSH", "subject": "Bilateral Vestibulopathy/embryology"}
{"id": "https://id.nlm.nih.gov/mesh/D000071699Q000201", "scheme": "MeSH", "subject": "Bilateral Vestibulopathy/enzymology"}
{"id": "https://id.nlm.nih.gov/mesh/D000071699Q000453", "scheme": "MeSH", "subject": "Bilateral Vestibulopathy/epidemiology"}
{"id": "https://id.nlm.nih.gov/mesh/D000071699Q000209", "scheme": "MeSH", "subject": "Bilateral Vestibulopathy/etiology"}
{"id": "https://id.nlm.nih.gov/mesh/D000071699Q000235", "scheme": "MeSH", "subject": "Bilateral Vestibulopathy/genetics"}
{"id": "https://id.nlm.nih.gov/mesh/D000071699Q000266", "scheme": "MeSH", "subject": "Bilateral Vestibulopathy/history"}
{"id": "https://id.nlm.nih.gov/mesh/D000071699Q000276", "scheme": "MeSH", "subject": "Bilateral Vestibulopathy/immunology"}
{"id": "https://id.nlm.nih.gov/mesh/D000071699Q000378", "scheme": "MeSH", "subject": "Bilateral Vestibulopathy/metabolism"}
{"id": "https://id.nlm.nih.gov/mesh/D000071699Q000382", "scheme": "MeSH", "subject": "Bilateral Vestibulopathy/microbiology"}
{"id": "https://id.nlm.nih.gov/mesh/D000071699Q000401", "scheme": "MeSH", "subject": "Bilateral Vestibulopathy/mortality"}
{"id": "https://id.nlm.nih.gov/mesh/D000071699Q000451", "scheme": "MeSH", "subject": "Bilateral Vestibulopathy/nursing"}
```