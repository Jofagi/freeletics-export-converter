# freeletics-export-converter

Extremely simple converter for converting the trainings list of a freeletics
export YAML to CSV for further processing.

# Obtain Data Export
On the freeletics.com website one can export the data that freeletics has
stored about the user.
Currently, clicking the export button will forward to a customer support
request form, where the export needs to be requested.
After a day one will receive a link to a file called `fl_uid_XXXXXX_at_NNNNNN`,
which is a compressed archive containing a `text_data.yml`.

# Converting
Extract the data export archive, place `text_data.yml` next to `convert.py` and
then call `python convert.py` from that directory. The result will be a
`training.csv`. That's it.
