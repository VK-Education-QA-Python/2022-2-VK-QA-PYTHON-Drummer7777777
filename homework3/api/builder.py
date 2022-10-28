from dataclasses import dataclass
import time


class Builder:
    @staticmethod
    def create_company(id_content):
        @dataclass
        class CreateCompany:
            company_name = f'Company name {time.time()}'
            title_banner = 'Title'
            text_banner = 'Text'
            id_created_company = None
            data = {
                "name": company_name,
                "objective": "general_ttm",
                "package_id": 451,
                "banners": [
                    {
                        "urls": {
                            "primary": {
                                "id": 2992
                            }
                        },
                        "textblocks": {
                            "title_25": {
                                "text": title_banner
                            },
                            "text_90": {
                                "text": text_banner
                            },
                            "cta_sites_full": {
                                "text": "visitSite"
                            }
                        },
                        "content": {
                            "image_90x75": {
                                "id": id_content
                            }
                        },
                        "name": ""
                    }
                ]
            }
        return CreateCompany
    @staticmethod
    def create_segment(relations_object_type, source_id):
        @dataclass
        class CreateSegment:
            if relations_object_type == "remarketing_player":
                relations = [
                        {"object_type":"remarketing_player",
                         "params":
                             {"type":"positive",
                              "left":365,
                              "right":0
                              }
                         }
                    ]
            if relations_object_type == "remarketing_vk_group":
                relations = [
                    {
                        "object_type":"remarketing_vk_group",
                        "params":{
                            "source_id":source_id,
                            "type":"positive"
                        }
                    }
                ]
            data = {
                "name":f"Test{time.time()}",
                "pass_condition":1,
                "relations": relations,
                "logicType":"or"
            }
            id_segment = None
            id_group_in_found_list = None
        return CreateSegment