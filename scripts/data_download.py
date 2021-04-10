import boto3
import os

HOST_NAME           = 'http://public.services.aad.gov.au'
BUCKET_NAME         = 'datasets'
ACCESS_KEY          = '473c624225d64e9da479125c1e5645be010'
SECRET_ACCESS_KEY   = 'e10465ca06a34a2bbb546fa0e1aa22f2014'
REMOTE_FILE_PATH    = 'science/AcousticTrends_BlueFinLibrary/'
LOCAL_FILE_PATH     = 'data/'

def download_files(subdirectory=''):
    if not os.path.isdir(LOCAL_FILE_PATH + subdirectory):
        os.mkdir(LOCAL_FILE_PATH + subdirectory)

    #initiate s3 resource
    session = boto3.session.Session()
    s3 = session.resource(
        service_name='s3',
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_ACCESS_KEY,
        endpoint_url=HOST_NAME,
    )

    # select bucket
    bucket = s3.Bucket(BUCKET_NAME)

    # download file into current directory
    print('Downloading files from ' + REMOTE_FILE_PATH + subdirectory)
    for s3_object in bucket.objects.filter(Delimiter='/', Prefix=REMOTE_FILE_PATH + subdirectory):
        # Need to split s3_object.key into path and file name, else it will give error file not found.
        path, filename = os.path.split(s3_object.key)
        bucket.download_file(s3_object.key, LOCAL_FILE_PATH + subdirectory + filename)


# There *should* be a boto3 method to list subfolders in a bucket/directory, which would allow us to simply 
#   recurse through the top level REMOTE_FILE_PATH directory. But I haven't found this method...
#   So instead, just explicitly download files from the known subdirectories.
download_files()

print('\n')
download_files('01-Documentation/')
download_files('01-Documentation/Subsampling/')
download_files('01-Documentation/Subsampling/subsampleLowFrequencyFixedRate/')
download_files('01-Documentation/Subsampling/subsampleLowFrequencyFixedRate/annotatedLibrary/')
download_files('01-Documentation/Subsampling/subsampleLowFrequencyFixedRate/soundFolder/')
download_files('01-Documentation/Subsampling/subsampleLowFrequencyFixedRate/stats/')
download_files('01-Documentation/Subsampling/subsampleLowFrequencyFixedRate/utilsBSM/')

print('\n')
download_files('02-AnnotationSettings/')

print('\n')
download_files('03-PamguardSettings/')
download_files('03-PamguardSettings/energyDetection_Bp20/')
download_files('03-PamguardSettings/spectrogramCorr_annotation_Ant-ABZ//')

print('\n')
download_files('BallenyIslands2015/')
download_files('BallenyIslands2015/wav/')

print('\n')
download_files('ElephantIsland2013Aural/')
download_files('ElephantIsland2013Aural/IWC_SelectionTables_Balcazar2019/')
download_files('ElephantIsland2013Aural/wav/')

print('\n')
download_files('ElephantIsland2014/')
download_files('ElephantIsland2014/wav/')

print('\n')
download_files('Greenwich64S2015/')
download_files('Greenwich64S2015/AWI-SV1057-2015_Raven_Selections/')
download_files('Greenwich64S2015/wav/')

print('\n')
download_files('MaudRise2014/')
download_files('MaudRise2014/MaudRise2014_RavenAnnotations_SORP_Library/')
download_files('MaudRise2014/wav/')

print('\n')
download_files('RossSea2014/')
download_files('RossSea2014/exemplarcallsRoss2014/')
download_files('RossSea2014/wav/')

print('\n')
download_files('casey2014/')
download_files('casey2014/wav/')

print('\n')
download_files('casey2017/')
download_files('casey2017/Annotated library/')
download_files('casey2017/wav/')

print('\n')
download_files('kerguelen2005/')
download_files('kerguelen2005/wav/')

print('\n')
download_files('kerguelen2014/')
download_files('kerguelen2014/wav/')

print('\n')
download_files('kerguelen2015/')
download_files('kerguelen2015/wav/')