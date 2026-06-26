from azure.search.documents.indexes.models import (
    SearchIndexerDataSourceConnection,
    SearchIndexerDataContainer,
    HighWaterMarkChangeDetectionPolicy
)
"""
def data_source_connection(
    data_source_name: str,
    container_name: str,
    storage_connection_string: str
):
    container = SearchIndexerDataContainer(name=container_name)

    data_source_connection = SearchIndexerDataSourceConnection(
        name=data_source_name,
        type="azureblob",
        connection_string=storage_connection_string,
        container=container,
        data_change_detection_policy=HighWaterMarkChangeDetectionPolicy(
            high_water_mark_column_name="metadata_storage_last_modified"
        )
        # 🚫 no deletion policy for blob
    )

    return data_source_connection
"""


def data_source_connection( data_source_name: str, container_name: str, storage_connection_string: str ): 
    container = SearchIndexerDataContainer(name=container_name) 
    data_source_connection = SearchIndexerDataSourceConnection( name=data_source_name, type="azureblob", 
                                                               connection_string=storage_connection_string, 
                                                               container=container ) 
    return data_source_connection