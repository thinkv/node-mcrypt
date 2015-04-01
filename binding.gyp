{
    "targets": [
        {
            "target_name": "mcrypt",
            "sources": [
                "src/mcrypt.cc"
            ],
            "include_dirs": [
                "/usr/include/",
                "/opt/local/include/",
                "/app/.apt/usr/lib/",
                "/.apt/usr/lib/"
            ],
            "link_settings": {
                "libraries": [
                    "-lmcrypt"
                ]
            }
        }
    ]
}
