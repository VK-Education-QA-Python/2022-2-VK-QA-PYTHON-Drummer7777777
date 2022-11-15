import pytest
from base import ApiBase


class TestApi(ApiBase):
    authorize = True
    @pytest.mark.API
    def test_api_create_company(self, api_client, file_path):
        id_content = self.api_client.upload_image(file_path)
        id_created_company = self.api_client.create_company(id_content)
        exist = self.api_client.check_created_company(id_created_company=id_created_company)
        if exist: self.api_client.delete_company(id_created_company)

    @pytest.mark.API
    def test_api_creat_segment(self, api_client):
        id_segment = self.api_client.create_segment("remarketing_player")
        exist = self.api_client.check_created_segment(id_segment)
        if exist: self.api_client.delete_segment(id_segment)

    @pytest.mark.API
    def test_api_create_segment_with_VK_group(self,api_client):
        id_group_in_found_list, id_segment_group_vk = self.api_client.add_vk_group()
        id_segment = self.api_client.create_segment("remarketing_vk_group", source_id=id_group_in_found_list)
        exist = self.api_client.check_created_segment(id_segment)
        if exist: self.api_client.delete_segment(id_segment)
        self.api_client.delete_segment_group_vk(id_segment_group_vk)
