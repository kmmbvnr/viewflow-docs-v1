====================================
Workflow automation suite for Django
====================================

.. warning::

    Please, login with any social account


Login
=====

.. raw:: html

    <div id="loginBox" style="font-size:84px;height:700px">
        <a href="/login/github/"><i class="fa fa-github-square"></i></a>
        <a href="/login/bitbucket/"><i class="fa fa-bitbucket-square"></i></a>
        <!--a href="/login/facebook/"><i class="fa fa-facebook-square"></i></a-->
        <!--a href="/login/google-oauth2/"><i class="fa fa-google-plus-square"></i></a>
        <a href="/login/linkedin-oauth2/"><i class="fa fa-linkedin-square"></i></a-->
        <a href="/login/reddit/"><i class="fa fa-reddit-square"></i></a>
        <a href="/login/twitter/"><i class="fa fa-twitter-square"></i></a>
    </div>
    <script>
        $('#loginBox a').each(function() { 
                $(this).attr('href', $(this).attr('href')+"?next="+document.location.toString()) 
        });
    </script>
