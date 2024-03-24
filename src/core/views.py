from dependency_injector.wiring import Provide, inject
from django.http import HttpResponse
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from config.container import CoreContainer
from core.interfaces.services.core import CoreServiceInterface
from core.serializers import ItemSerializer


class CreateCheckAPIView(GenericAPIView):
    serializer_class = ItemSerializer

    @inject
    def post(
        self,
        request: Request,
        core_service: CoreServiceInterface = Provide[CoreContainer.core_service],
    ) -> HttpResponse:
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            ids = serializer.validated_data['items']
            file_name = core_service.build_pdf_file(ids=ids)
            qr_code_img = core_service.get_qr_code_img(
                scheme=request.stream.scheme,
                host=request.stream.get_host(),
                file_name=file_name,
            )

            return HttpResponse(content=qr_code_img, content_type='image/jpeg')
        else:
            return Response(status=400)
