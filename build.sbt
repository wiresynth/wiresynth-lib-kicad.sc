ThisBuild / scalaVersion := "3.7.1"
ThisBuild / organization := "io.github.wiresynth.sc"

ThisBuild / versionScheme := Some("semver-spec")

ThisBuild / homepage := Some(url("https://github.com/wiresynth"))
ThisBuild / licenses := List(
  "MIT " -> url(
    "https://www.gnu.org/licenses/old-licenses/lgpl-2.1-standalone.html"
  )
)
ThisBuild / developers := List(
  Developer(
    "jellyterra",
    "Jelly Terra",
    "jellyterra@jellyterra.com",
    url("https://jellyterra.com")
  )
)

val coreVersion = "0.1.0"

val root = (project in file("."))
  .settings(
    Compile / scalaSource := baseDirectory.value / "src",
    name := "lib-kicad",
    libraryDependencies ++= Seq(
      "io.github.wiresynth.sc" %% "core" % coreVersion,
      compilerPlugin("io.github.wiresynth.sc" %% "plugin" % coreVersion)
    )
  )
