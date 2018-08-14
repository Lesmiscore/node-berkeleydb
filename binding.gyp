{
  "targets": [
    {
      "target_name": "addon",
      "sources": [
        "src/addon.cc",
        "src/db.cc",
        "src/dbenv.cc",
        "src/dbtxn.cc",
        "src/dbcursor.cc"
      ],
      "include_dirs": [
        "../include",
        "<!(node -e \"require('nan')\")",
        "./deps/db-4.8.30.NC/build_unix"
      ],
      "link_settings": {
        "libraries": [
          "-L../lib",
          "-L../deps/db-4.8.30.NC/build_unix",
          "-ldb-4.8"
        ]
      }
    }
  ]
}
