#!/usr/bin/env python3
"""
org/acmsl/licdata/application/licdata_app.py

This file runs Licdata server.

Copyright (C) 2023-today ACM S.L. Licdata-Application

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from org.acmsl.licdata import Client
from org.acmsl.licdata.infrastructure.clients.github import GithubClientRepo
from org.acmsl.licdata.infrastructure.incidents.github import GithubIncidentRepo
from org.acmsl.licdata.infrastructure.licenses.github import GithubLicenseRepo
from org.acmsl.licdata.infrastructure.orders.github import GithubOrderRepo
from org.acmsl.licdata.infrastructure.pcs.github import GithubPcRepo
from org.acmsl.licdata.infrastructure.prelicenses.github import GithubPrelicenseRepo
from org.acmsl.licdata.infrastructure.products.github import GithubProductRepo
from org.acmsl.licdata.infrastructure.product_types.github import GithubProductTypeRepo
from org.acmsl.licdata.infrastructure.users.github import GithubUserRepo
from pythoneda.shared.application import PythonEDA, enable
import asyncio


@enable(GithubClientRepo)
@enable(GithubIncidentRepo)
@enable(GithubLicenseRepo)
@enable(GithubOrderRepo)
@enable(GithubPcRepo)
@enable(GithubPrelicenseRepo)
@enable(GithubProductRepo)
@enable(GithubProductTypeRepo)
@enable(GithubUserRepo)
class LicdataApp(PythonEDA):
    """
    Runs Licdata.

    Class name: LicdataApp

    Responsibilities:
        - Launch Licdata from the command line.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new instance.
        """
        # licdata_app_banner is automatically generated by the Nix flake.
        try:
            from org.acmsl.licdata.application.licdata_app_banner import (
                LicdataAppBanner,
            )

            banner = LicdataAppBanner()
        except ImportError:
            banner = None

        super().__init__(banner, __file__)

    async def accept_new_client_requested(self, event):
        """
        Receives a request to create a new client.
        :param event: The event.
        :type event: org.acmsl.licdata.events.NewClientRequested
        """
        created = await Client.listen_NewClientRequested(event)
        if created:
            await self.emit(created)
        return created


if __name__ == "__main__":
    asyncio.run(LicdataApp.main())
