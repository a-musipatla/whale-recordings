# Whale Sound Exploration

This repository explores interesting features of the Acoustic Trends Blue Fin Library [1], which consists of annotated recordings of Antarctic baleen whale sounds. The data is publicly available under a Creative Commons 4.0 Attribution licence. It is accessible via the Australian Antarctic Data Centre at http://data.aad.gov.au/metadata/records/AcousticTrends_BlueFinLibrary.

## Installation

**Downloading Data**
0. The contents of the dataset can be viewed in your browser [here](https://data.aad.gov.au/s3/bucket/datasets/science/AcousticTrends_BlueFinLibrary/), though they cannot be downloaded straight from this site. 
1. Request access keys for the Australian Antarctic Data Centre's (AADC) S3 host/bucket [here](https://data.aad.gov.au/eds/5091/download).
    - You should receive an email from the AADC containing an access key and a secret key. 
    - Edit `scripts/download_data.py`, change `ACCESS_KEY` and `SECRET_ACCESS_KEY` to the key values you received via email.
2. In this repo, create a directory `data/` at the top level.
    - Alternately, you can change `LOCAL_FILE_PATH` in `scripts/download_data.py` to your desired download path and create that repository. 
3. From this repo, run `python download_data.py`

## Usage


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Citations

[1] Miller, B.S., Stafford, K.M., Van Opzeeland, I., Harris, D., Samaran, F., šIrović, A., Buchan, S., Findlay, K., Balcazar, N., Nieukirk , S., Leroy, E.C., Aulich, M., Shabangu, F.W., Dziak, R.P., Lee, W., Hong, J. (2020) An annotated library of underwater acoustic recordings for testing and training automated algorithms for detecting Antarctic blue and fin whale sounds, Ver. 1, Australian Antarctic Data Centre - doi:10.26179/5e6056035c01b, Accessed: 2021-04-09 (https://www.nature.com/articles/s41598-020-78995-8)