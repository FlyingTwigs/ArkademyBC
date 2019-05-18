<?php
require_once('.main/query.php')
$query = new DBquery();

?>

<!DOCTYPE html>
<html>
<head>
    <title> Database </title>
</head>
<body>
    <strong> Tambah Programmer </strong>
    <table border="1">
        <tr>
            <form method="POST" action="add.php?action=addUsers">
                <td>Enter your name please</td>
                <td>
                    <input name="addusers" type="text">
                    <input type="submit" name="add" value="add">
                </td>
            </form>
        </tr>
    </table>
    <strong> Skill </strong>
    <table border="1" width="30%">
        <tr>
            <th> Nama </th>
            <th> Skill </th>
            <th> + </th>
        </tr>
        <?php
            foreach($query->getUserSkills() as $row):
        ?>
        <tr>
            <td> <?= $row['name'] ?> </td>
            <td>
                <?php
                    if($row[1] == ".") {
                        echo "Belum ditambahkan";
                    } else {
                        echo $row[1];
                    }
                ?> </td>
            <form method="POST" action="add.php?action=update">
                <td>
                    <input name="id" type="hidden" value="<?= $row['id'] ?>">
                    <input name="skill" type="text">
                    <input type="submit" name="update" values="tambahkan">
                </td>
            </form>
        </tr>
        <?php
            endforeach;
        ?>
    </table>
