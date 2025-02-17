import unittest
from solution import solution

# Level 1: Basic operations (FILE_UPLOAD, FILE_GET, FILE_COPY) and error conditions
class Level1(unittest.TestCase):
    def test_basic_operations(self):
        test_data = [
            ["FILE_UPLOAD", "FileA.txt", "100kb"],
            ["FILE_GET", "FileA.txt"],
            ["FILE_COPY", "FileA.txt", "FileB.txt"],
            ["FILE_GET", "FileB.txt"]
        ]
        output = solution(test_data)
        self.assertEqual(output, [
            "uploaded FileA.txt",
            "got FileA.txt",
            "copied FileA.txt to FileB.txt",
            "got FileB.txt"
        ])

    def test_error_conditions(self):
        test_data = [
            ["FILE_UPLOAD", "Duplicate.txt", "100kb"],
            ["FILE_UPLOAD", "Duplicate.txt", "100kb"],
            ["FILE_COPY", "NonExistent.txt", "Copy.txt"],
            ["FILE_GET", "NonExistent.txt"]
        ]
        output = solution(test_data)
        self.assertEqual(output, [
            "uploaded Duplicate.txt",
            "error: file already exists",
            "error: source file not found",
            "file not found"
        ])

    def test_self_copy(self):
        test_data = [
            ["FILE_UPLOAD", "SelfCopy.txt", "110kb"],
            ["FILE_COPY", "SelfCopy.txt", "SelfCopy.txt"],
            ["FILE_GET", "SelfCopy.txt"]
        ]
        output = solution(test_data)
        self.assertEqual(output, [
            "uploaded SelfCopy.txt",
            "copied SelfCopy.txt to SelfCopy.txt",
            "got SelfCopy.txt"
        ])

    def test_overwrite_copy(self):
        test_data = [
            ["FILE_UPLOAD", "FileX.txt", "100kb"],
            ["FILE_UPLOAD", "FileY.txt", "150kb"],
            ["FILE_COPY", "FileX.txt", "FileY.txt"],
            ["FILE_GET", "FileY.txt"]
        ]
        output = solution(test_data)
        self.assertEqual(output, [
            "uploaded FileX.txt",
            "uploaded FileY.txt",
            "copied FileX.txt to FileY.txt",
            "got FileY.txt"
        ])

# Level 2: Data processing (FILE_SEARCH) and ordering
class Level2(unittest.TestCase):
    def test_search_ordering(self):
        test_data = [
            ["FILE_UPLOAD", "Alpha.txt", "50kb"],
            ["FILE_UPLOAD", "Alpine.txt", "60kb"],
            ["FILE_UPLOAD", "Beta.txt", "70kb"],
            ["FILE_UPLOAD", "Alphabet.txt", "55kb"],
            ["FILE_SEARCH", "Al"]
        ]
        output = solution(test_data)
        self.assertEqual(output, [
            "uploaded Alpha.txt",
            "uploaded Alpine.txt",
            "uploaded Beta.txt",
            "uploaded Alphabet.txt",
            "found [Alpine.txt, Alphabet.txt, Alpha.txt]"
        ])

    def test_additional_search(self):
        test_data = [
            ["FILE_UPLOAD", "Search1.txt", "80kb"],
            ["FILE_UPLOAD", "TestFile.txt", "90kb"],
            ["FILE_UPLOAD", "AnotherSearch.txt", "70kb"],
            ["FILE_SEARCH", "NonExistent"],
            ["FILE_SEARCH", ""]
        ]
        output = solution(test_data)
        self.assertEqual(output, [
            "uploaded Search1.txt",
            "uploaded TestFile.txt",
            "uploaded AnotherSearch.txt",
            "found []",
            "found [TestFile.txt, Search1.txt, AnotherSearch.txt]"
        ])

    def test_search_no_files(self):
        test_data = [
            ["FILE_SEARCH", "Any"]
        ]
        output = solution(test_data)
        self.assertEqual(output, [
            "found []"
        ])

    def test_search_case_sensitivity(self):
        test_data = [
            ["FILE_UPLOAD", "Test.txt", "100kb"],
            ["FILE_SEARCH", "T"],
            ["FILE_SEARCH", "t"]
        ]
        output = solution(test_data)
        self.assertEqual(output, [
            "uploaded Test.txt",
            "found [Test.txt]",
            "found []"
        ])

# Level 3: Timestamped operations and TTL handling
class Level3(unittest.TestCase):
    def test_ttl_boundaries(self):
        test_data = [
            ["FILE_UPLOAD_AT", "2022-01-01T00:00:00", "TTLTest.txt", "200kb", "5"],
            ["FILE_GET_AT", "2022-01-01T00:00:04", "TTLTest.txt"],
            ["FILE_GET_AT", "2022-01-01T00:00:05", "TTLTest.txt"],
            ["FILE_GET_AT", "2022-01-01T00:00:06", "TTLTest.txt"]
        ]
        output = solution(test_data)
        self.assertEqual(output, [
            "uploaded TTLTest.txt",
            "got TTLTest.txt",
            "got TTLTest.txt",
            "file not found"
        ])

    def test_complex_mix_operations(self):
        test_data = [
            ["FILE_UPLOAD_AT", "2022-02-01T12:00:00", "Mix1.txt", "150kb"],
            ["FILE_UPLOAD_AT", "2022-02-01T12:00:00", "Mix2.txt", "200kb", "3600"],
            ["FILE_COPY_AT", "2022-02-01T12:00:00", "Mix1.txt", "Mix1Copy.txt"],
            ["FILE_SEARCH_AT", "2022-02-01T12:00:00", "Mix"],
            ["FILE_GET_AT", "2022-02-01T12:59:59", "Mix2.txt"],
            ["FILE_GET_AT", "2022-02-01T13:00:01", "Mix2.txt"]
        ]
        output = solution(test_data)
        self.assertEqual(output, [
            "uploaded Mix1.txt",
            "uploaded Mix2.txt",
            "copied Mix1.txt to Mix1Copy.txt",
            "found [Mix2.txt, Mix1Copy.txt, Mix1.txt]",
            "got Mix2.txt",
            "file not found"
        ])

    def test_same_timestamp_ordering(self):
        test_data = [
            ["FILE_UPLOAD_AT", "2022-04-01T10:00:00", "SameTime1.txt", "100kb"],
            ["FILE_UPLOAD_AT", "2022-04-01T10:00:00", "SameTime2.txt", "150kb"],
            ["FILE_UPLOAD_AT", "2022-04-01T10:00:00", "SameTime3.txt", "150kb"],
            ["FILE_SEARCH_AT", "2022-04-01T10:00:00", "SameTime"]
        ]
        output = solution(test_data)
        self.assertEqual(output, [
            "uploaded SameTime1.txt",
            "uploaded SameTime2.txt",
            "uploaded SameTime3.txt",
            "found [SameTime3.txt, SameTime2.txt, SameTime1.txt]"
        ])

    def test_complex_sequence(self):
        test_data = [
            ["FILE_UPLOAD_AT", "2022-06-01T15:00:00", "Normal.txt", "100kb"],
            ["FILE_UPLOAD_AT", "2022-06-01T15:00:01", "Temp.txt", "80kb", "10"],
            ["FILE_COPY_AT", "2022-06-01T15:00:02", "Normal.txt", "NormalCopy.txt"],
            ["FILE_SEARCH_AT", "2022-06-01T15:00:02", "N"],
            ["FILE_GET_AT", "2022-06-01T15:00:05", "Temp.txt"],
            ["FILE_GET_AT", "2022-06-01T15:00:12", "Temp.txt"]
        ]
        output = solution(test_data)
        self.assertEqual(output, [
            "uploaded Normal.txt",
            "uploaded Temp.txt",
            "copied Normal.txt to NormalCopy.txt",
            "found [NormalCopy.txt, Normal.txt]",
            "got Temp.txt",
            "file not found"
        ])

    def test_infinite_ttl(self):
        test_data = [
            ["FILE_UPLOAD_AT", "2022-07-01T11:00:00", "Infinite.txt", "500kb"],
            ["FILE_GET_AT", "2022-07-01T11:00:00", "Infinite.txt"],
            ["FILE_GET_AT", "2022-07-01T12:00:00", "Infinite.txt"]
        ]
        output = solution(test_data)
        self.assertEqual(output, [
            "uploaded Infinite.txt",
            "got Infinite.txt",
            "got Infinite.txt"
        ])

    def test_duplicate_timestamp_upload(self):
        test_data = [
            ["FILE_UPLOAD_AT", "2022-08-01T10:00:00", "DupFile.txt", "100kb"],
            ["FILE_UPLOAD_AT", "2022-08-01T10:05:00", "DupFile.txt", "150kb"]
        ]
        output = solution(test_data)
        self.assertEqual(output, [
            "uploaded DupFile.txt",
            "error: file already exists"
        ])

    def test_timestamp_copy_nonexistent(self):
        test_data = [
            ["FILE_COPY_AT", "2022-08-01T11:00:00", "Nonexistent.txt", "Copy.txt"]
        ]
        output = solution(test_data)
        self.assertEqual(output, [
            "error: source file not found"
        ])

    def test_copy_expired_timestamp(self):
        test_data = [
            ["FILE_UPLOAD_AT", "2022-10-01T10:00:00", "ExpireFile.txt", "200kb", "5"],
            ["FILE_COPY_AT", "2022-10-01T10:00:06", "ExpireFile.txt", "ExpireFileCopy.txt"]
        ]
        output = solution(test_data)
        self.assertEqual(output, [
            "uploaded ExpireFile.txt",
            "error: source file not found"
        ])

    def test_overwrite_copy_at(self):
        test_data = [
            ["FILE_UPLOAD_AT", "2022-11-01T09:00:00", "SourceFile.txt", "100kb"],
            ["FILE_UPLOAD_AT", "2022-11-01T09:00:00", "DestFile.txt", "150kb"],
            ["FILE_COPY_AT", "2022-11-01T09:05:00", "SourceFile.txt", "DestFile.txt"],
            ["FILE_GET_AT", "2022-11-01T09:05:00", "DestFile.txt"]
        ]
        output = solution(test_data)
        self.assertEqual(output, [
            "uploaded SourceFile.txt",
            "uploaded DestFile.txt",
            "copied SourceFile.txt to DestFile.txt",
            "got DestFile.txt"
        ])

# Level 4: Rollback operations
class Level4(unittest.TestCase):
    def test_rollback_functionality(self):
        test_data = [
            ["FILE_UPLOAD_AT", "2022-03-01T08:00:00", "Rollback1.txt", "120kb"],
            ["FILE_UPLOAD_AT", "2022-03-01T08:05:00", "Rollback2.txt", "130kb", "600"],
            ["FILE_COPY_AT", "2022-03-01T08:10:00", "Rollback1.txt", "Rollback1Copy.txt"],
            ["ROLLBACK", "2022-03-01T08:05:00"],
            ["FILE_GET_AT", "2022-03-01T08:10:00", "Rollback2.txt"],
            ["FILE_SEARCH_AT", "2022-03-01T08:10:00", "Rollback"]
        ]
        output = solution(test_data)
        self.assertEqual(output, [
            "uploaded Rollback1.txt",
            "uploaded Rollback2.txt",
            "copied Rollback1.txt to Rollback1Copy.txt",
            "rollback to 2022-03-01T08:05:00",
            "got Rollback2.txt",
            "found [Rollback2.txt, Rollback1.txt]"
        ])

    def test_multiple_rollback(self):
        test_data = [
            ["FILE_UPLOAD_AT", "2022-05-01T09:00:00", "Multi1.txt", "100kb"],
            ["FILE_UPLOAD_AT", "2022-05-01T09:05:00", "Multi2.txt", "200kb", "300"],
            ["ROLLBACK", "2022-05-01T09:00:00"],
            ["FILE_UPLOAD_AT", "2022-05-01T09:06:00", "Multi3.txt", "150kb"],
            ["FILE_COPY_AT", "2022-05-01T09:06:00", "Multi1.txt", "Multi1Copy.txt"],
            ["FILE_SEARCH_AT", "2022-05-01T09:06:00", "Multi"]
        ]
        output = solution(test_data)
        self.assertEqual(output, [
            "uploaded Multi1.txt",
            "uploaded Multi2.txt",
            "rollback to 2022-05-01T09:00:00",
            "uploaded Multi3.txt",
            "copied Multi1.txt to Multi1Copy.txt",
            "found [Multi3.txt, Multi1Copy.txt, Multi1.txt]"
        ])

    def test_rollback_ttl_adjustment(self):
        test_data = [
            ["FILE_UPLOAD_AT", "2022-12-01T10:00:00", "TempTTL.txt", "100kb", "300"],
            ["FILE_GET_AT", "2022-12-01T10:04:00", "TempTTL.txt"],
            ["ROLLBACK", "2022-12-01T10:00:00"],
            ["FILE_GET_AT", "2022-12-01T10:06:00", "TempTTL.txt"]
        ]
        output = solution(test_data)
        self.assertEqual(output, [
            "uploaded TempTTL.txt",
            "got TempTTL.txt",
            "rollback to 2022-12-01T10:00:00",
            "file not found"
        ])

    def test_rollback_removes_later_files(self):
        test_data = [
            ["FILE_UPLOAD_AT", "2022-12-01T11:00:00", "FutureFile.txt", "100kb"],
            ["ROLLBACK", "2022-12-01T10:59:59"],
            ["FILE_GET_AT", "2022-12-01T11:00:00", "FutureFile.txt"]
        ]
        output = solution(test_data)
        self.assertEqual(output, [
            "uploaded FutureFile.txt",
            "rollback to 2022-12-01T10:59:59",
            "file not found"
        ])

    def test_rollback_overwrite(self):
        test_data = [
            ["FILE_UPLOAD_AT", "2022-03-01T08:00:00", "Rollback1.txt", "120kb"],
            ["FILE_UPLOAD_AT", "2022-03-01T08:05:00", "Rollback2.txt", "130kb"],
            ["FILE_COPY_AT", "2022-03-01T08:10:00", "Rollback1.txt", "Rollback2.txt"],
            ["ROLLBACK", "2022-03-01T08:05:00"],
            ["FILE_GET_AT", "2022-03-01T08:10:00", "Rollback2.txt"],
            ["FILE_SEARCH_AT", "2022-03-01T08:10:00", "Rollback"]
        ]
        output = solution(test_data)
        self.assertEqual(output, [
            "uploaded Rollback1.txt",
            "uploaded Rollback2.txt",
            "copied Rollback1.txt to Rollback2.txt",
            "rollback to 2022-03-01T08:05:00",
            "got Rollback2.txt",
            "found [Rollback2.txt, Rollback1.txt]"
        ])

if __name__ == '__main__':
    unittest.main()