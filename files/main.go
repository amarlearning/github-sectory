package files

import (
	"io"
	"os"
	"strings"
)

func Write(filepath string, data io.ReadCloser) error {
	err := createFile(filepath)
	if err != nil {
		return err
	}

	out, err := os.OpenFile(filepath, os.O_CREATE|os.O_WRONLY|os.O_APPEND, os.ModePerm)
	if err != nil {
		return err
	}

	defer out.Close()

	_, err = io.Copy(out, data)
	if err != nil {
		return err
	}

	return nil
}

func createFile(filepath string) error {
	directoryPath := getDirPath(filepath)
	if !exist(filepath) {
		err := os.MkdirAll(directoryPath, 0755)
		if err != nil {
			return err
		}

		_, er := os.Create(filepath)
		if er != nil {
			return er
		}
	}

	return nil
}

func exist(path string) bool {
	_, err := os.Stat(path)
	if err == nil || os.IsExist(err) {
		return true
	}

	if os.IsNotExist(err) {
		return false
	}
	return false
}

func getDirPath(filepath string) (directoryPath string) {
	split := strings.Split(filepath, "/")
	filename := split[len(split)-1]
	split = strings.Split(filepath, filename)
	directoryPath = split[0][:len(split[0])-1]
	return
}
