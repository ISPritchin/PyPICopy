import fastapi
from fastapi_chameleon import template
from starlette.requests import Request

from viewmodels.home.index_viewmodel import IndexViewModel
from viewmodels.shared.viewmodel import ViewModelBase

router = fastapi.APIRouter()


@router.get('/')
@template(template_file='home/index.pt')
def index(request: Request):
    vm = IndexViewModel(request)
    return vm.to_dict()


@router.get('/about')
@template(template_file='home/about.pt')
def about(request: Request):
    vm = ViewModelBase(request)
    return vm.to_dict()
