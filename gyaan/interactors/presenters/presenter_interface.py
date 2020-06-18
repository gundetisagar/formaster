from abc import abstractmethod
from gyaan.exceptions.exceptions import InvalidPostIds
from gyaan.dtos.dtos import DomainDetailsDTO
from gyaan.interactors.storages.dtos import CompletePostDetailsDTO
    
from gyaan.dtos.dtos import DomainDetailsWithPostsDTO


class PresenterInterface:

    @abstractmethod
    def raise_domain_does_not_exist_exception(self):
        pass

    @abstractmethod
    def raise_user_not_domain_member_exception(self, error):
        pass

    @abstractmethod
    def get_domain_details_response(self,
                                    domain_details_dto: DomainDetailsDTO):
        pass

    @abstractmethod
    def raise_exception_for_invalid_post_ids(self, error: InvalidPostIds):
        pass

    @abstractmethod
    def get_posts_response(self,
                           completed_post_details_dto: CompletePostDetailsDTO):
        pass

    @abstractmethod
    def get_domain_posts_response(self, post_details: CompletePostDetailsDTO):
        pass

    @abstractmethod
    def get_domain_with_posts_response(
            self, domain_details_with_posts: DomainDetailsWithPostsDTO):
        pass
